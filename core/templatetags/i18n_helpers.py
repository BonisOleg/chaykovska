"""i18n helper template tags."""
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def get_available_languages():
    """Return tuple of available languages from settings."""
    return settings.LANGUAGES


@register.simple_tag(takes_context=True)
def get_language_code(context):
    """Return current language code from request."""
    request = context.get('request')
    if request:
        return request.LANGUAGE_CODE
    return settings.LANGUAGE_CODE
