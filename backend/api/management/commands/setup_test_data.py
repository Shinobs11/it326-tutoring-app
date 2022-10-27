# https://mattsegal.dev/django-factoryboy-dummy-data.html
from django.db import transaction
from django.core.management.base import BaseCommand

from api.models.User import User
from api.factories.UserFactory import UserFactory

NUM_USERS = 30
NUM_STUDENTS = 15
NUM_TUTORS = 15
NUM_MANAGERS = 15

class Command(BaseCommand):
  help = "Generates test data"

  # Using the transaction.atomic decorator makes a big difference in the runtime of this script,
  # since it bundles up 100s of queries and submits them in one go.
  @transaction.atomic
  def handle(self, *args, **kwargs):
    self.stdout.write("Deleting old data...")
    models = [User]
    for m in models:
      m.objects.all().delete()
    

    self.stdout.write("Creating new data...")
    users = []
    for _ in range(NUM_USERS):
      users.append(UserFactory())

    

