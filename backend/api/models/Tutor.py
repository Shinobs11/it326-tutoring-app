from django.db import models
from api.models.User import User
import uuid
class Tutor(models.Model):

  class Meta:
    app_label = 'api'


  
  user = models.OneToOneField(User, primary_key=True, db_index=True,  on_delete=models.CASCADE)
  # tutorID = models.UUIDField(primary_key=True,default=uuid.uuid4 ,editable=False, unique=True, db_index=True, null=False, blank=False)

  


