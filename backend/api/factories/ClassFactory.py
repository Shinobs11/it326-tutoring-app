import factory
from factory.django import DjangoModelFactory
from api.models.Class import Class
import datetime
from random import sample, randint

class ClassFactory(DjangoModelFactory):

  class Meta:
    model = Class
  #classID - auto
  #className - argument
  classDescription = factory.Faker('text', max_nb_chars=1500)