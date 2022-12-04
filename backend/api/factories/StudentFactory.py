import factory
from factory.django import DjangoModelFactory
from api.models.Student import Student, YEAR_CHOICE_ENUM
from api.models.User import User
from faker import Faker


fake = Faker() 
Faker.seed(0)
class StudentFactory(DjangoModelFactory):
  class Meta:
    model = Student




  studentID = factory.Faker("uuid4")
  # yearInSchool = fake.random_element(elements=Student.YearInSchool.choices)[0]
  yearInSchool = factory.Faker('random_element', elements=[x[0] for x in Student.YearInSchool.choices])



  # tutorSessHours = factory.Faker("tutorSessHours")
  