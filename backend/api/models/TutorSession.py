from django.db import models
from api.models.Class import Class
from api.models.Tutor import Tutor
from api.models.Student import Student
from django.utils.timezone import now
import uuid
from api.models.TutorOrganization import TutorOrganization

class TutorSession(models.Model):


  class Meta:
    app_label = 'api'


  tutorSessID = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
  classID = models.ManyToManyField(Class, blank=True)
  tutorOrgID = models.ForeignKey(TutorOrganization, null=True, on_delete=models.CASCADE)

  tutor = models.ManyToManyField(Tutor, blank=True)
  student = models.ManyToManyField(Student, blank=True)

  date = models.DateTimeField(default=now)
  sessName = models.CharField(blank=False,null=False,max_length=50, unique=True)
  location= models.CharField(max_length=100, null=True)
  conferenceURL = models.URLField(max_length=256, null=True)

