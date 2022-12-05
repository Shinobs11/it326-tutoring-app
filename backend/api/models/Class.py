from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from api.models.Student import Student
import uuid

class Class(models.Model):

  class Meta:
    app_label = 'api'

  #PK, Only class IDs b/w 100-999 are allowed
  classID = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
  className = models.CharField(max_length=12, null=False, blank=True, editable=True)
  classDescription = models.CharField(max_length=1500, null=True, editable=True)