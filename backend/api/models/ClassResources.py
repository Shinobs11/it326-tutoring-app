from django.db import models
from api.models.Class import Class


class ClassResources(models.Model):
  class Meta:
    app_label = 'api'

  #OPTIONAL 1-M with Class
  classID = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)
  resourceID = models.PositiveSmallIntegerField(primary_key=True)
  name = models.CharField(max_length=20, blank=False)
