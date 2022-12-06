from django.db import models
from api.models.TutorSession import TutorSession
import uuid

class SessionResource(models.Model):
  class Meta:
    app_label = 'api'
    # unique_together=(('sessionID', 'resourceID'),)
    constraints=[
      models.UniqueConstraint(fields=['sessionID', 'resourceID'], name='sessionID_resourceID_pk')
    ]

  #OPTIONAL 1-M with Class
  sessionID = models.ForeignKey(TutorSession, on_delete=models.CASCADE, blank=True, null=True)
  resourceID = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20, blank=False)
  content = models.CharField(max_length=5000, blank=False)