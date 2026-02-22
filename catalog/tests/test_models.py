from django.test import TestCase
from ..models import Category, Product, ProductImage


class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Dresses',
            slug='dresses'
        )
    
    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Dresses')


class ProductTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name='Dresses',
            slug='dresses'
        )
        self.product = Product.objects.create(
            name='Evening Dress',
            description='Beautiful evening dress',
            price=1500.00,
            category=self.category
        )
    
    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Evening Dress')
        self.assertTrue(self.product.is_available)
