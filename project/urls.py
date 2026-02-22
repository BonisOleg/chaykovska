"""
URL configuration for chaykovska project.
"""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('pages.urls')),
    path('catalog/', include('catalog.urls')),
    path('cart/', include('cart.urls')),
    prefix_default_language=True,
)

# Serve media files in development
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
