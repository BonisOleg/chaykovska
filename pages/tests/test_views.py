from django.test import TestCase
from django.urls import reverse
from ..models import MosaicCell, AboutSection


class PagesViewTest(TestCase):
    def test_home_view(self):
        """Test home page renders."""
        response = self.client.get(reverse('pages:home'))
        self.assertEqual(response.status_code, 200)
    
    def test_about_view(self):
        """Test about page renders."""
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)
    
    def test_contacts_view(self):
        """Test contacts page renders."""
        response = self.client.get(reverse('pages:contacts'))
        self.assertEqual(response.status_code, 200)
