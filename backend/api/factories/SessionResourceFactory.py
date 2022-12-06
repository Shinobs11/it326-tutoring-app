from faker import Faker
import factory
from factory.django import DjangoModelFactory
from api.models.SessionResource import SessionResource


class SessionResourceFactory(DjangoModelFactory):

  class Meta:
    model = SessionResource
  sessionID = None
  name = factory.Faker('text', max_nb_chars=20)
  content = factory.Faker('text', max_nb_chars=2000)
