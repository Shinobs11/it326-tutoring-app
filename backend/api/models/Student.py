from enum import Enum
from django.db import models

import uuid

YEAR_CHOICE_ENUM = Enum('year_choice', ['Freshman', 'Sophomore', 'Junior', 'Senior'])

class Student(models.Model):

  class Meta:
    app_label = 'api'

# https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-choices-enum-types
  class YearInSchool(models.IntegerChoices):
    FRESHMAN = 0, 'Freshman'
    SOPHOMORE = 1, 'Sophomore'
    JUNIOR = 2, 'Junior'
    SENIOR = 3, 'Senior'
    GRADUATE = 4, 'Graduate'
    NOT_APPLICABLE = 5, 'N/A'
  #PK
  studentID = models.UUIDField(primary_key=True,  editable=False, unique=True, db_index=True, null=False, blank=False)
  yearInSchool = models.SmallIntegerField(default=None, editable=True, null=True, choices=YearInSchool.choices)


  # tutorSessHours= models.PositiveSmallIntegerField(default=0)



