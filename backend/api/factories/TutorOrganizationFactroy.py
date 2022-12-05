import factory
from factory.django import DjangoModelFactory
from api.models.TutorOrganization import TutorOrganization
import random
class TutorOrganizationFactory(DjangoModelFactory):
  class Meta:
    model = TutorOrganization
  

  #tutOrgID - auto-generated
  tutOrgName = factory.Faker('text',
  max_nb_chars=random.randint(7, 30)
  )
  tutOrgDescription = factory.Faker('text',
  max_nb_chars=1500
  )

