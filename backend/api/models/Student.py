from django.db import models
from api.models.User import User

class Student(models.Model):

  class Meta:
    app_label = 'api'

  #OPTIONAL 1-1 relation with User
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  #PK
  studentID = models.PositiveSmallIntegerField(primary_key=True, blank=False, null=False)
  tutorSessHours= models.PositiveSmallIntegerField(default=0)



