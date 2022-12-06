from faker import Faker
import factory
from factory.django import DjangoModelFactory
from api.models.Message import Message


class MessageFactory(DjangoModelFactory):

  class Meta:
    model = Message

  text = factory.Faker('text', max_nb_chars=800)
  inbox = None
  timestamp = factory.Faker('date_time_this_month', after_now=True)