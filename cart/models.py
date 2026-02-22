from django.db import models
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    """Customer order."""
    
    STATUS_CHOICES = [
        ('new', _('New')),
        ('processing', _('Processing')),
        ('shipped', _('Shipped')),
        ('delivered', _('Delivered')),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Order #{self.id} - {self.first_name} {self.last_name}'
    
    def get_total(self):
        """Calculate order total."""
        return sum(item.get_subtotal() for item in self.items.all())


class OrderItem(models.Model):
    """Item in an order."""
    
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        'catalog.Product',
        on_delete=models.SET_NULL,
        null=True
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Price at time of order'
    )
    
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
    
    def __str__(self):
        return f'{self.product.name} x {self.quantity}'
    
    def get_subtotal(self):
        """Calculate subtotal for this item."""
        return self.price * self.quantity
