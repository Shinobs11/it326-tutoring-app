from django.db import models
from api.models.TutorOrgManager import TutorOrgManager
from api.models.Tutor import Tutor
import uuid


class TutorOrganization(models.Model):
  class Meta:
    app_label = 'api'

  tutOrgID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True, null=False, blank=False)
  #MANDATORY M-M relation with Tutor
  tutor = models.ManyToManyField(Tutor)
  # MANDATORY M-M relation with TutorOrgManager
  tutOrgMan = models.ManyToManyField(TutorOrgManager, blank=False)
  tutOrgName = models.CharField(unique=True, max_length=30)