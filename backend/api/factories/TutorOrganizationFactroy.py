from factory.django import DjangoModelFactory
from api.models.TutorOrganization import TutorOrganization

class TutorOrganizationFactory(DjangoModelFactory):
  class Meta:
    model = TutorOrganization
  
  