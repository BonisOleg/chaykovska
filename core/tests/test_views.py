from django.test import TestCase
from django.urls import reverse


class CoreViewTest(TestCase):
    def test_language_switching(self):
        """Test language switching URL."""
        response = self.client.get(reverse('core:set_language'))
        self.assertIn(response.status_code, [200, 302, 405])
