import factory
from factory.django import DjangoModelFactory
from api.models.Tutor import Tutor
from api.models.User import User


class TutorFactory(DjangoModelFactory):
    class Meta:
        model = Tutor

    user = factory.SubFactory(User)
    tutorID = factory.Faker("tutorID")
    rating = factory.Faker("rating")
    tutor_subj = factory.Faker("tutor_subj")
    Num_Tut_Orgs = factory.Faker("Num_Tut_Orgs")
