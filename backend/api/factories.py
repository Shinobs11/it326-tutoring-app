# https://mattsegal.dev/django-factoryboy-dummy-data.html

import factory
from factory.django import DjangoModelFactory
from .models import Student, User

class UserFactory(DjangoModelFactory):
  class Meta:
    model = User
  
  

  first_name = factory.Faker("first_name")
  last_name = factory.Faker("last_name")
  email_address = factory.Faker("email")
  phone_number = factory.Faker("phone_number")

class StudentFactory(DjangoModelFactory):
  class Meta:
    model = Student
  
  