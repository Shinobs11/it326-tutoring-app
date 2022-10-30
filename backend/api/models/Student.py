from django.db import models
from api.models import User

class Student(models.Model):
  #OPTIONAL 1-1 relation with User
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    blank=True, null=True
  )
  #PK
  studentID = models.PositiveSmallIntegerField(primary_key=True, blank=False, null=False)


