from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonModelAdmin):
    pass
