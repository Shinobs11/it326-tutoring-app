from django.db import models
from api.models.User import User
class TutorOrgManager(models.Model):



  class Meta:
    app_label = 'api'

  # OPTIONAL 1-1 relation with User
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    blank = True, null = True
  )
  tutOrgManID = models.PositiveSmallIntegerField(primary_key=True)
