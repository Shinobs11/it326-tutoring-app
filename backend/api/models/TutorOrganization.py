from django.db import models
from api.models.TutorOrgManager import TutorOrgManager
from api.models.Tutor import Tutor



class TutorOrganization(models.Model):
  class Meta:
    app_label = 'api'

  tutOrgID = models.PositiveSmallIntegerField(primary_key=True)
  #MANDATORY M-M relation with Tutor
  tutor = models.ManyToManyField(Tutor, blank=False)
  # MANDATORY M-M relation with TutorOrgManager
  tutOrgMan = models.ManyToManyField(TutorOrgManager, blank=False)
  tutOrgName = models.CharField(unique=True, max_length=30)