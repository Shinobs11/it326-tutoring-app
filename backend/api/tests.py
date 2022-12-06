from django.test import TestCase

# Create your tests here.
from api.models.Student import Student
from api.models.TutorSession import TutorSession
from django.test import RequestFactory, TestCase
from api.Fstudent import Fstudent
from api.management.commands.setup_test_data import Command
from django.core.management import call_command


class RateTutorSessionTest(TestCase):
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
    
    response = Fstudent.rate(request)
    self.assertEqual(response.status_code, 200)