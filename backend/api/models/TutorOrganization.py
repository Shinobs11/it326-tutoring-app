from django.db import models
from api.models.TutorOrgManager import TutorOrgManager
from api.models.Tutor import Tutor
from api.models.TutorSession import TutorSession
import uuid


class TutorOrganization(models.Model):
  class Meta:
    app_label = 'api'

  tutOrgID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True, null=False, blank=False)
  #OPTIONAL M-M relation with Tutor
  tutor = models.ManyToManyField(Tutor)
  #OPTIONAL M-M relation with TutorOrgManager
  tutOrgMan = models.ManyToManyField(TutorOrgManager, blank=False)
  #OPTIONAL 1-M with TutorSession
  tutSess = models.ForeignKey(TutorSession, blank=True, null=True, on_delete=models.CASCADE)
  tutOrgName = models.CharField(unique=True, max_length=30)
