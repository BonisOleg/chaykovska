"""Pages app factories."""
from factory import django as factory_django, Faker
from .models import MosaicCell, AboutSection, ContactInfo


class MosaicCellFactory(factory_django.DjangoModelFactory):
    class Meta:
        model = MosaicCell
    
    position = Faker('random_int', min=1, max=12)
    size_type = 'half'


class AboutSectionFactory(factory_django.DjangoModelFactory):
    class Meta:
        model = AboutSection
    
    section_type = 'brand'
    title = Faker('sentence')
    content = Faker('paragraph')


class ContactInfoFactory(factory_django.DjangoModelFactory):
    class Meta:
        model = ContactInfo
    
    address = Faker('address')
    phone = Faker('phone_number')
    email = Faker('email')
    working_hours = '9am - 6pm'
