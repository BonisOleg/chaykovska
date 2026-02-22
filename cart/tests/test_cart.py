from django.test import TestCase
from django.urls import reverse
from cart.utils import SessionCart
from catalog.factories import ProductFactory, CategoryFactory


class CartTest(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.product = ProductFactory(category=self.category)
    
    def test_cart_view(self):
        """Test cart page renders."""
        response = self.client.get(reverse('cart:cart'))
        self.assertEqual(response.status_code, 200)
    
    def test_add_to_cart(self):
        """Test adding product to cart."""
        session = self.client.session
        cart = SessionCart(session)
        cart.add(self.product.id, quantity=2)
        session.save()
        
        self.assertEqual(cart.get_count(), 2)
    
    def test_remove_from_cart(self):
        """Test removing product from cart."""
        session = self.client.session
        cart = SessionCart(session)
        cart.add(self.product.id, quantity=1)
        cart.remove(self.product.id)
        session.save()
        
        self.assertEqual(cart.get_count(), 0)
