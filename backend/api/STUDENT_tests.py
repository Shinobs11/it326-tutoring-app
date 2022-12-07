from django.test import TestCase

# Create your tests here.
from api.models.Student import Student
from api.models.TutorSession import TutorSession
from api.models.Review import Review
from django.test import RequestFactory, TestCase
from api.Fstudent import Fstudent
from api.management.commands.setup_test_data import Command
from django.core.management import call_command


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