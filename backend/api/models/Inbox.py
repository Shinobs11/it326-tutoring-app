from django.db import models
from api.models.User import User

class Inbox(models.Model):

  class Meta:
    app_label = 'api'

  #MANDATORY 1-1 with User
  user = models.OneToOneField(User, primary_key=True, db_index=True, on_delete=models.CASCADE)

