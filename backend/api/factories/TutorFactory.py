import factory
from factory.django import DjangoModelFactory
from api.models.Tutor import Tutor


class TutorFactory(DjangoModelFactory):
    class Meta:
        model = Tutor

    # rating = factory.Faker("rating")
    # tutor_subj = factory.Faker("tutor_subj")
    # Num_Tut_Orgs = factory.Faker("Num_Tut_Orgs")