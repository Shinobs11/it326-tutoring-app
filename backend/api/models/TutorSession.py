from django.db import models
from api.models.Class import Class
from api.models.Tutor import Tutor
from api.models.Student import Student
from django.utils.timezone import now
class TutorSession(models.Model):


  class Meta:
    app_label = 'api'
  #OPTIONAL M-M with Tutor
  tutor = models.ManyToManyField(Tutor, blank=True, null=True)
  # OPTIONAL M- M with TutorOrgManager
  student = models.ManyToManyField(Student, blank=True, null=True)
  #MANDATORY 1-M relation with Class
  classID = models.ForeignKey(Class,blank=False, null=False, on_delete=models.DO_NOTHING)
  tutorSessID = models.PositiveSmallIntegerField(primary_key=True)
  date = models.DateTimeField(default=now)
  sessName = models.CharField(blank=False,null=False,max_length=50)