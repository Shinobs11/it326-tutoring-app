from django.db import models
from api.models.TutorSession import TutorSession


class SessionResources(models.Model):
  class Meta:
    app_label = 'api'
    unique_together=(('classID', 'resourceID'),)

  #OPTIONAL 1-M with Class
  sessionID = models.ForeignKey(TutorSession, on_delete=models.CASCADE, blank=True, null=True)
  resourceID = models.PositiveSmallIntegerField(primary_key=True)
  name = models.CharField(max_length=20, blank=False)
  content = models.CharField(max_length=100000, blank=False)