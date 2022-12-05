# https://mattsegal.dev/django-factoryboy-dummy-data.html
from faker import Faker
import factory
from factory.django import DjangoModelFactory
from api.models.User import User
from .TutorFactory import TutorFactory
from ..models.TutorOrgManager import TutorOrgManager



class UserFactory(DjangoModelFactory):


  def __init__(self, is_tutor: bool, is_student: bool, is_tutorOrgManager: bool) -> None:
    super().__init__()
    self.Params.is_tutor = is_tutor
    self.Params.is_student = is_student
    self.Params.is_tutorOrgManager = is_tutorOrgManager


  class Meta:
    model = User

    
  class Params:
    is_tutor = False
    is_student = False
    is_tutorOrgManager = False

  
  uid = factory.Faker("uuid4")
  first_name = factory.Faker("first_name")
  last_name = factory.Faker("last_name")
  email_address = factory.Faker("email")
  phone_number = factory.Faker("phone_number")
  password = factory.Faker("password")



  # soluTION IS TO COMBINE RELATED FACTORY WITH THE MAYBE THING TO CONDITIONALLY GENERATE FACTORIES WITH A GIVEN USER
  # https://factoryboy.readthedocs.io/en/latest/reference.html#post-generation-hooks
  # factory.Maybe(decider='is_tutor', yes_declaration=factory.RelatedFactory('api.factories.TutorFactory', factory_related_name='user'), no_declaration= None)
  # factory.Maybe(decider='is_student', yes_declaration=factory.RelatedFactory('api.factories.StudentFactory', factory_related_name='user'), no_declaration= None)
  # factory.Maybe(decider='is_tutorOrgManager', yes_declaration=factory.RelatedFactory('api.factories.TutorOrgManagerFactory', factory_related_name='user'), no_declaration= None)
  
  #this sucks so if there's a better way lmk
  # tutor = factory.Maybe(decider='is_tutor', yes_declaration=factory.SubFactory('api.factories.TutorFactory'), no_declaration=None)
  # student = factory.Maybe(decider='is_student', yes_declaration=factory.SubFactory('api.factories.StudentFactory'), no_declaration=None)
  # tutorOrgManager = factory.Maybe(decider='is_tutorOrgManager', yes_declaration=factory.SubFactory('api.factories.TutorOrgManagerFactory'), no_declaration=None)


