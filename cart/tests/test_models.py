from django.test import TestCase
from ..models import Order, OrderItem
from catalog.models import Category, Product


class OrderTest(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            first_name='John',
            last_name='Doe',
            phone='+380501234567',
            email='john@example.com',
            address='Kyiv, Ukraine'
        )
    
    def test_order_creation(self):
        self.assertEqual(self.order.first_name, 'John')
        self.assertEqual(self.order.status, 'new')


class CartTest(TestCase):
    def setUp(self):
        self.client.cookies.clear()
    
    def test_empty_cart(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
