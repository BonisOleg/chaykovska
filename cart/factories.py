"""Cart app factories."""
from factory import django as factory_django, Faker
from .models import Order, OrderItem


class OrderFactory(factory_django.DjangoModelFactory):
    class Meta:
        model = Order
    
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    phone = Faker('phone_number')
    email = Faker('email')
    address = Faker('address')
    status = 'new'


class OrderItemFactory(factory_django.DjangoModelFactory):
    class Meta:
        model = OrderItem
    
    order = factory_django.SubFactory(OrderFactory)
    quantity = Faker('random_int', min=1, max=5)
    price = Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
