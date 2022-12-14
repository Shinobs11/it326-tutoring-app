from django.db import models
from api.models.TutorOrgManager import TutorOrgManager
from api.models.Tutor import Tutor
import uuid


class TutorOrganization(models.Model):
  class Meta:
    app_label = 'api'

  tutOrgID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True, null=False, blank=False)
  tutor = models.ManyToManyField(Tutor, blank=True)
  tutOrgMan = models.ManyToManyField(TutorOrgManager, blank=False)
  tutOrgName = models.CharField(unique=True, max_length=30)
  tutOrgDescription = models.CharField(max_length=1500, default="")

  
