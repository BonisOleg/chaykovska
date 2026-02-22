"""Session-based shopping cart utility."""


class SessionCart:
    """Manage shopping cart via Django session."""
    
    SESSION_KEY = 'shopping_cart'
    
    def __init__(self, session):
        self.session = session
    
    def add(self, product_id, quantity=1):
        """Add product to cart."""
        cart = self.session.get(self.SESSION_KEY, {})
        
        if str(product_id) in cart:
            cart[str(product_id)]['quantity'] += quantity
        else:
            from catalog.models import Product
            product = Product.objects.get(id=product_id)
            cart[str(product_id)] = {
                'product_id': product_id,
                'quantity': quantity,
                'price': str(product.price),
                'name': product.name,
            }
        
        self.session[self.SESSION_KEY] = cart
        self.session.modified = True
    
    def remove(self, product_id):
        """Remove product from cart."""
        cart = self.session.get(self.SESSION_KEY, {})
        
        if str(product_id) in cart:
            del cart[str(product_id)]
            self.session[self.SESSION_KEY] = cart
            self.session.modified = True
    
    def update_quantity(self, product_id, quantity):
        """Update product quantity."""
        if quantity <= 0:
            self.remove(product_id)
        else:
            cart = self.session.get(self.SESSION_KEY, {})
            if str(product_id) in cart:
                cart[str(product_id)]['quantity'] = quantity
                self.session[self.SESSION_KEY] = cart
                self.session.modified = True
    
    def get_items(self):
        """Get all cart items."""
        cart = self.session.get(self.SESSION_KEY, {})
        from catalog.models import Product
        
        items = []
        for product_id, item in cart.items():
            try:
                product = Product.objects.get(id=int(product_id))
                items.append({
                    'product': product,
                    'quantity': item['quantity'],
                    'price': item['price'],
                    'subtotal': float(item['price']) * item['quantity'],
                })
            except Product.DoesNotExist:
                pass
        
        return items
    
    def get_total(self):
        """Get cart total."""
        return sum(item['subtotal'] for item in self.get_items())
    
    def get_count(self):
        """Get total number of items in cart."""
        return sum(item['quantity'] for item in self.get_items())
    
    def clear(self):
        """Clear entire cart."""
        if self.SESSION_KEY in self.session:
            del self.session[self.SESSION_KEY]
            self.session.modified = True
