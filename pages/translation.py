from modeltranslation.translator import translator, TranslationOptions
from .models import MosaicCell, AboutSection, ContactInfo


class MosaicCellTranslationOptions(TranslationOptions):
    fields = ()


class AboutSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


class ContactInfoTranslationOptions(TranslationOptions):
    fields = ('address', 'working_hours')


translator.register(MosaicCell, MosaicCellTranslationOptions)
translator.register(AboutSection, AboutSectionTranslationOptions)
translator.register(ContactInfo, ContactInfoTranslationOptions)
