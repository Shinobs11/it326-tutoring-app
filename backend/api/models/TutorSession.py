from django.db import models
from api.models.Class import Class
from api.models.Tutor import Tutor
from api.models.Student import Student
from django.utils.timezone import now
class TutorSession(models.Model):


  class Meta:
    app_label = 'api'
  #OPTIONAL M-M with Tutor
  tutor = models.ManyToManyField(Tutor, blank=True)
  # OPTIONAL M- M with TutorOrgManager
  student = models.ManyToManyField(Student, blank=True)
  #MANDATORY 1-M relation with Class
  classID = models.ForeignKey(Class,blank=False, null=True, on_delete=models.DO_NOTHING)
  tutorSessID = models.PositiveSmallIntegerField(primary_key=True)
  date = models.CharField(max_length=50)#changing from datetime field, don't know how to work with Dates in htmls
  sessName = models.CharField(blank=False,null=False,max_length=50, unique=True)
