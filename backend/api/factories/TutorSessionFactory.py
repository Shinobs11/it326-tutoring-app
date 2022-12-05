import factory
from factory.django import DjangoModelFactory
from api.models.TutorSession import TutorSession
from django.utils.timezone import make_aware
from datetime import datetime


class TutorSessionFactory(DjangoModelFactory):
    class Meta:
        model = TutorSession

    #tutorSessID - auto
    #classID - m-m
    #tutorOrg = o-m

    #tutor - m-m
    #student - m-m

    date = factory.Faker('date_time_this_month', after_now=True)
    sessName = factory.Faker('text', 
      max_nb_chars=50
    )
    location = factory.Faker(
      'address'
    )
    conferenceURL = factory.Faker(
      'uri'
    )
