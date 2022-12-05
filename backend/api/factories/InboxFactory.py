from faker import Faker
import factory
from factory.django import DjangoModelFactory
from api.models.Inbox import Inbox


class InboxFactory(DjangoModelFactory):

  class Meta:
    model = Inbox


