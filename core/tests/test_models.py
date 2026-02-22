from django.test import TestCase
from ..models import SiteSettings


class SiteSettingsTest(TestCase):
    def test_singleton_instance(self):
        """Test that only one instance of SiteSettings can exist."""
        settings1 = SiteSettings.objects.get_or_create()[0]
        settings2 = SiteSettings.objects.get_or_create()[0]
        self.assertEqual(settings1.pk, settings2.pk)
