from django.test import TestCase
from django.urls import reverse
from ..models import Category, Product
from ..factories import CategoryFactory, ProductFactory


class CatalogViewTest(TestCase):
    def setUp(self):
        self.category = CategoryFactory()
        self.product = ProductFactory(category=self.category)
    
    def test_catalog_view(self):
        """Test catalog list view."""
        response = self.client.get(reverse('catalog:catalog'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
    
    def test_product_detail_view(self):
        """Test product detail view."""
        response = self.client.get(reverse('catalog:product_detail', kwargs={'slug': self.product.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
