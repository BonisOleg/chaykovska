from modeltranslation.translator import translator, TranslationOptions
from .models import Order


class OrderTranslationOptions(TranslationOptions):
    fields = ()


translator.register(Order, OrderTranslationOptions)
