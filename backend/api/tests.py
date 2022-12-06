from django.test import TestCase

# Create your tests here.
from api.Ftutor import Ftutor
from api.models.Tutor import Tutor
from api.models.TutorSession import TutorSession
from api.models.TutorOrganization import TutorOrganization
from django.test import RequestFactory, TestCase
from api.management.commands.setup_test_data import Command
from django.core.management import call_command


class testStudent(TestCase):
  fixtures = ['fixture.json']

  def setUp(self):
    self.factory = RequestFactory()