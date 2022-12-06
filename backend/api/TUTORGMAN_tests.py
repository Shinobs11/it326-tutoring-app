from django.test import TestCase

# Create your tests here.
from api.FtutorOrgManager import FtutorOrgManager
from api.FtutorOrg import FtutorOrg
from api.models.Student import Student
from api.models.TutorOrganization import TutorOrganization
from api.models.TutorOrgManager import TutorOrgManager
from api.models.TutorSession import TutorSession
from api.models.Class import Class
from api.models.Tutor import Tutor
from api.models.SessionResource import SessionResource
from django.test import RequestFactory, TestCase
from api.management.commands.setup_test_data import Command
from django.core.management import call_command


class testStudent(TestCase):
  fixtures = ['fixture.json']

  def setUp(self):
    self.factory = RequestFactory()
  
  def test_createTutorSession(self):
    # Tutor Organization
    org = TutorOrganization.objects.all()[0]
    orgName = org.tutOrgName

    # The Request we're making
    request = self.factory.post('createSession',
      {
        'name': orgName,
        'date': "2022-12-25T15:31:12",
        'SessName': "Fernando's Comp Sci Tutoring Session"
      }
    )

    response = FtutorOrg.createSession(request)
    self.assertEquals(response.status_code, 200)

  def test_insertClassResource(self):
    # Tutor Session
    tutSes = TutorSession.objects.all()[0]
    session = tutSes.sessName

    request = self.factory.post('insertResource',
      {
        'className': "IT 326",
        'classData': "Slides 10_15",
        'sessName': session
      }
    )

    response = FtutorOrg.insertResource(request)
    self.assertEquals(response.status_code, 200)

  def test_removeTutorSession(self):
    # Tutor Session
    session = TutorSession.objects.all()[0]
    sess = session.sessName

    request = self.factory.post('removeSession',
      {
        'SessName': session
      }
    )

    response = FtutorOrg.removeSession(request)
    self.assertEquals(response.status_code, 200)

  def test_removeUserFromSession(self):
    # Session
    session = TutorSession.objects.all()[0]
    sess = session.sessName

    # Student
    student = session.student.all()[0]
    user = student.user
    email_address = user.email_address


    request = self.factory.post('removeuser',
      {
        'name': sess,
        'email': email_address
      }
    )
    

    response = FtutorOrgManager.removeUser(request)
    self.assertEquals(response.status_code, 200)

  def test_addClassToSession(self):
    # Session
    session = TutorSession.objects.all()[0]
    sess = session.sessName

    request = self.factory.post('addClassToSession',
      {
        'className': "IT 326",
        'classDesc': "TutorTim Rocks!",
        'sessName': sess
      }
    )

    response = FtutorOrg.addClasstoSession(request)
    self.assertEquals(response.status_code, 200)


  def test_addTutorToSession(self):
    # Tutor
    tutor = Tutor.objects.all()[0]
    user = tutor.user
    email_address = user.email_address

    # Session
    session = TutorSession.objects.all()[0]
    sess = session.sessName

    request = self.factory.post('addTutorToSession',
      {
        'tutorEmail': email_address,
        'sessName': sess,
      }
    )

    response = FtutorOrg.addTutorToSession(request)
    self.assertEquals(response.status_code, 200)

  def test_createTutorOrg(self):
    # Tutor Org Manager
    tutorOrgManager = TutorOrgManager.objects.all()[0]
    user = tutorOrgManager.user

    # Variables we are passing
    email_address = user.email_address

    # The Request we're making
    request = self.factory.post('createTutorOrg',
      {
        'email': email_address,
        'name': "The Tutor Org for Comp Sci",
        'desc': "We teach Java, Python, and C++!"
      }
    )

    response = FtutorOrgManager.createTutorOrg(request)
    self.assertEquals(response.status_code, 200)