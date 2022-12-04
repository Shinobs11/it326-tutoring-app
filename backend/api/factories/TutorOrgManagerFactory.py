import factory
from factory.django import DjangoModelFactory
from api.models.TutorOrgManager import TutorOrgManager


class TutorOrgManagerFactory(DjangoModelFactory):
    class Meta:
        model = TutorOrgManager


    tutOrgManID = factory.Faker("uuid4")
    # rating = factory.Faker("rating")
    # tutor_subj = factory.Faker("tutor_subj")
    # Num_Tut_Orgs = factory.Faker("Num_Tut_Orgs")
