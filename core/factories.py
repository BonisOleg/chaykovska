"""Core app factories."""
from factory import django as factory_django
from .models import SiteSettings


class SiteSettingsFactory(factory_django.DjangoModelFactory):
    class Meta:
        model = SiteSettings
