from django.db import models
from api.models.User import User
import uuid

class TutorOrgManager(models.Model):

  class Meta:
    app_label = 'api'

  # OPTIONAL 1-1 relation with User

  user = models.OneToOneField(User, primary_key=True, db_index=True, on_delete=models.CASCADE)