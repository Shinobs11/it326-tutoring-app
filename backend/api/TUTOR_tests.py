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
  
  def test_registerForTutorOrg(self):
    # Tutor
    tutor = Tutor.objects.all()[0]
    user = tutor.user
    email_address = user.email_address

    # Tutor Organization
    org = TutorOrganization.objects.all()[0]
    orgName = org.tutOrgName

    request = self.factory.post('registerOrgtut',
      {
        'email': email_address,
        'name': orgName
      }
    )

    response = Ftutor.registerOrgtut(request)
    self.assertEquals(response.status_code, 200)

  def test_registerForTutorSess(self):
    # Tutor
    tutor = Tutor.objects.all()[0]
    user = tutor.user
    email_address = user.email_address

    # Tutor Session
    tutSes = TutorSession.objects.all()[0]
    session = tutSes.sessName

    request = self.factory.post('registersesstut',
      {
        'email': email_address,
        'name': session
      }
    )

    response = Ftutor.registerTutorSess(request)
    self.assertEquals(response.status_code, 200)

  def test_unenrollOrganization(self):
    # Tutor
    tutor = Tutor.objects.all()[0]
    user = tutor.user
    email_address = user.email_address

    # Tutor Organization
    org = TutorOrganization.objects.all()[0]
    orgName = org.tutOrgName

    request = self.factory.post('unregisterFromOrg',
      {
        'email': email_address,
        'name': orgName
      }
    )

    response = Ftutor.unregisterFromOrg(request)
    self.assertEquals(response.status_code, 200)