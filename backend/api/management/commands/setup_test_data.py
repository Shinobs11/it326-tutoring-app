# https://mattsegal.dev/django-factoryboy-dummy-data.html
from django.db import transaction
from django.core.management.base import BaseCommand

from api.models import *
from api.factories.UserFactory import UserFactory
from api.factories.StudentFactory import StudentFactory
from api.factories.TutorFactory import TutorFactory
from api.factories.TutorOrgManagerFactory import TutorOrgManagerFactory
import os
from random import sample


TOGGLE =  os.environ['GENERATE_NEW_DATA']

NUM_USERS = 60
NUM_STUDENTS = 30
NUM_TUTORS = 30
NUM_MANAGERS = 30

class Command(BaseCommand):
  help = "Generates test data"

  # Using the transaction.atomic decorator makes a big difference in the runtime of this script,
  # since it bundles up 100s of queries and submits them in one go.
  @transaction.atomic
  def handle(self, *args, **kwargs):
    # self.stdout.write("Deleting old data...")
    # models = [User, Tutor, TutorOrgManager, Student]
    # for m in models:
    #   m.objects.all().delete()
    if(not TOGGLE):
      pass

    self.stdout.write("Creating new data...")
    users: list[UserFactory]= []
    student_sample = sample(range(NUM_USERS), k=NUM_STUDENTS)
    tutor_sample = sample(range(NUM_USERS), k=NUM_TUTORS)
    manager_sample = sample(range(NUM_USERS), k=NUM_MANAGERS)

    student_range = [False]*NUM_USERS
    tutor_range = [False]*NUM_USERS
    manager_range = [False]*NUM_USERS

    for i in student_sample:
      student_range[i] = True
    for i in tutor_sample:
      tutor_range[i] = True
    for i in manager_sample:
      manager_range[i] = True

    for i in range(NUM_USERS):
      users.append(UserFactory(is_tutor=tutor_range[i], is_student=student_range[i], is_tutorOrgManager=manager_range[i]))


# https://stackoverflow.com/questions/66381042/how-to-assign-the-attribute-of-subfactory-instead-of-the-subfactory-itself
# https://factoryboy.readthedocs.io/en/latest/reference.html#maybe


    

