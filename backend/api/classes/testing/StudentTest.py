from django.test import TestCase
from api.classes.Student import Student
from api.classes.TutorSession import TutorSession
class StudentTest(TestCase):

    def ratingOOBTest(self):
        s = Student("TEST","TEST","TEST","TEST","1234567890","TEST@gmail.com",1, "TEST")
        ts = TutorSession()
        s.rateTutorSession(ts,-1)

    def ratingValidTest(self):
        s = Student("TEST", "TEST", "TEST", "TEST", "1234567890", "TEST@gmail.com", 1, "TEST")
        ts = TutorSession()
        s.rateTutorSession(ts, 4)

        #TODO - Waiting on functionality, use Django API test
    def joinTutorSession(self):
        pass