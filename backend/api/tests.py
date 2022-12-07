from django.test import TestCase

# Create your tests here.
from api.models.Student import Student
from api.models.TutorOrganization import TutorOrganization
from api.models.TutorOrgManager import TutorOrgManager
from api.Ftutor import Ftutor
from api.models.Tutor import Tutor
from api.models.TutorSession import TutorSession
from api.FtutorOrgManager import FtutorOrgManager
from api.FtutorOrg import FtutorOrg
from api.models.Review import Review
from django.test import RequestFactory, TestCase
from api.Fstudent import Fstudent
from api.models.Tutor import Tutor
from api.Fuser import Fuser
from api.models.User import User
from api.classes.User import CUser
from api.management.commands.setup_test_data import Command
from django.core.management import call_command

class testUser(TestCase):

  fixtures = ['fixture.json']
  def setUp(self):
    self.factory = RequestFactory()

  def test_createProfile(self):
    request = self.factory.post('createprofile',
                                {
                                  'Fname': "Fernando",
                                  'Lname': "Payan",
                                  'email': "fpayan@ilstu.edu",
                                  'Phone Number': "2108605423",
                                  'password': "nando",
                                  'password2': "nando",
                                  'usertype': 1
                                }
                                )

    response = Fuser.createProfile(request)
    self.assertEquals(response.status_code, 200)
  def test_authenticateUser(self):
    user = User.objects.all()[0]
    email = user.email_address
    password = user.password

    self.assertTrue(CUser.login(email,password))

  def test_searchForSession(self):
    sess = TutorSession.objects.all()[0]
    request = self.factory.post('searchSession',
                                {
                                  'TutSesName': sess.sessName
                                }
                                )
    response = Fuser.searchSession(request)
    self.assertEqual(response.status_code, 200)

  def test_deleteProfile(self):
    user = User.objects.all()[0]
    request = self.factory.post('deleteprofile',
                                {
                                  'email': user.email_address,
                                  'password':user.password
                                }
                                )
    response = Fuser.deleteProfile(request)
    self.assertEqual(response.status_code, 200)

  def test_searchForTutor(self):
    user = User.objects.all()[0]
    request = self.factory.post('searchtutor',
                                {
                                  'email': user.email_address
                                }
                                )
    response = Fuser.searchTutor(request)
    self.assertEqual(response.status_code, 200)

  def test_editProfile(self):
    user = User.objects.all()[0]
    request = self.factory.post('editProfile',
                                {
                                  'curEmail': user.email_address,
                                  'email': "TEST@COM",
                                  'phoneNumber': "0123456789",
                                  'password': "TEST",
                                  'repeat': "TEST"
                                }
                                )

    response = Fuser.editProfile(request)
    self.assertEquals(response.status_code, 200)


class testStudent(TestCase):
  fixtures = ['fixture.json']

  def setUp(self):
    self.factory = RequestFactory()

  def test_rateTutorSession(self):
    # Create an instance of a GET request.
    session = TutorSession.objects.all()[0]

    student = session.student.all()[0]
    user = student.user
    email_address = user.email_address

    request = self.factory.post('sendrating',
                                {
                                  'session': session.tutorSessID,
                                  'rating': 5,
                                  'email': email_address
                                }
                                )

    review = Review.objects.filter(
      tutSess=session.pk
    ).filter(
      student=student.pk
    ).first()

    if review:
      self.assertTrue(True)
    else:
      self.fail()

    response = Fstudent.rate(request)
    self.assertEqual(response.status_code, 200)

  def test_registerForSession(self):
    # Session
    session = TutorSession.objects.all()[0]
    sess = session.sessName

    # Student
    student = session.student.all()[0]
    user = student.user
    email_address = user.email_address

    # The Request we're making
    request = self.factory.post('registersess',
                                {
                                  'name': sess,
                                  'email': email_address
                                }
                                )

    response = Fstudent.registerSessPage(request)
    self.assertEquals(response.status_code, 200)

  def test_unenrollForSession(self):
    # Session
    session = TutorSession.objects.all()[0]
    sess = session.sessName

    # Student
    student = session.student.all()[0]
    user = student.user
    email_address = user.email_address

    # The Request we're making
    request = self.factory.post('unenrollSession',
                                {
                                  'sessName': sess,
                                  'stuEmail': email_address
                                }
                                )

    response = Fstudent.unenrollSession(request)
    self.assertEquals(response.status_code, 200)


class testTutorOrgMan(TestCase):
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


class testTutor(TestCase):
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