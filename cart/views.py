from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from .utils import SessionCart
from .models import Order, OrderItem
from .forms import CheckoutForm
from catalog.models import Product


class CartView(TemplateView):
    template_name = 'cart/cart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = SessionCart(self.request.session)
        context['items'] = cart.get_items()
        context['total'] = cart.get_total()
        return context


@method_decorator(require_POST, name='dispatch')
class AddToCartView(View):
    def post(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id, is_available=True)
            cart = SessionCart(request.session)
            cart.add(product_id, quantity=1)
            
            # Return updated cart counter (OOB swap)
            count = cart.get_count()
            response = HttpResponse(f'<span id="cart-count" class="cart-count">{count}</span>')
            response['HX-Reselect'] = '#cart-count'
            return response
        except Product.DoesNotExist:
            return HttpResponse(_('Product not found'), status=404)


@method_decorator(require_POST, name='dispatch')
class RemoveFromCartView(View):
    def post(self, request, product_id):
        cart = SessionCart(request.session)
        cart.remove(product_id)
        
        return redirect('cart:cart')


@method_decorator(require_POST, name='dispatch')
class UpdateCartView(View):
    def post(self, request, product_id):
        quantity = request.POST.get('quantity', 0)
        
        try:
            quantity = int(quantity)
            cart = SessionCart(request.session)
            cart.update_quantity(product_id, quantity)
        except (ValueError, TypeError):
            pass
        
        return redirect('cart:cart')


class CheckoutView(TemplateView):
    template_name = 'cart/checkout.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = SessionCart(self.request.session)
        context['items'] = cart.get_items()
        context['total'] = cart.get_total()
        context['form'] = CheckoutForm()
        return context
    
    def post(self, request, *args, **kwargs):
        cart = SessionCart(request.session)
        
        if not cart.get_items():
            return redirect('cart:cart')
        
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save()
            
            # Create order items
            for item in cart.get_items():
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price'],
                )
            
            # Send confirmation email
            send_order_confirmation(order)
            
            # Clear cart
            cart.clear()
            
            return redirect('cart:order_success', order_id=order.id)
        
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return render(request, self.template_name, context)


class OrderSuccessView(TemplateView):
    template_name = 'cart/order_success.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['order'] = Order.objects.get(id=self.kwargs['order_id'])
        except Order.DoesNotExist:
            pass
        return context


def send_order_confirmation(order):
    """Send order confirmation email."""
    subject = _(f'Order #{order.id} - CHAYKOVSKA')
    message = _('''
    Thank you for your order!
    
    Order ID: {order_id}
    Name: {name}
    Email: {email}
    Phone: {phone}
    Address: {address}
    
    Items:
    ''').format(
        order_id=order.id,
        name=f'{order.first_name} {order.last_name}',
        email=order.email,
        phone=order.phone,
        address=order.address
    )
    
    for item in order.items.all():
        message += f'\n- {item.product.name} x {item.quantity} = {item.get_subtotal()} ₴'
    
    message += f'\n\nTotal: {order.get_total()} ₴'
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [order.email],
            fail_silently=False,
        )
    except Exception as e:
        print(f'Error sending email: {e}')
