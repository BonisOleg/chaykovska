from modeltranslation.translator import translator, TranslationOptions
from .models import SiteSettings


class SiteSettingsTranslationOptions(TranslationOptions):
    fields = ()  # SiteSettings has no translatable fields


translator.register(SiteSettings, SiteSettingsTranslationOptions)
