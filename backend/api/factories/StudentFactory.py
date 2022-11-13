import factory
from factory.django import DjangoModelFactory
from api.models.Student import Student
from api.models.User import User

class StudentFactory(DjangoModelFactory):
  class Meta:
    model = Student

  user = factory.SubFactory(User)
  studentID = factory.Faker("studentID")
  tutorSessHours = factory.Faker("tutorSessHours")
  