import factory
from factory.django import DjangoModelFactory
from api.models.User import User
from api.models.Student import Student

class StudentFactory(DjangoModelFactory):
  class Meta:
    model = Student
  
  