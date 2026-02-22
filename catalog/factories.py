"""Catalog app factories."""
from factory import django as factory_django, Faker
from .models import Category, Product, ProductImage


class CategoryFactory(factory_django.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = Faker('word')
    slug = Faker('slug')


class ProductFactory(factory_django.DjangoModelFactory):
    class Meta:
        model = Product
    
    name = Faker('sentence', nb_words=3)
    description = Faker('paragraph')
    price = Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    category = factory_django.SubFactory(CategoryFactory)
    is_available = True


class ProductImageFactory(factory_django.DjangoModelFactory):
    class Meta:
        model = ProductImage
    
    product = factory_django.SubFactory(ProductFactory)
    position = Faker('random_int', min=0, max=5)
