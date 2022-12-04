from django.db import models

import uuid
class Tutor(models.Model):

  class Meta:
    app_label = 'api'


  

  tutorID = models.UUIDField(primary_key=True, editable=False, unique=True, db_index=True, null=False, blank=False)

  


