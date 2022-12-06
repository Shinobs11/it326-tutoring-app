from random import randint
from faker import Faker
import factory
from factory.django import DjangoModelFactory
from api.models.Review import Review
from random import randint

class ReviewFactory(DjangoModelFactory):

  class Meta:
    model = Review
  #ratingID auto
  
  student = None #o-o
  rating = None
  tutSess = None #many-to-one