from django.db import models
from api.models.Class import Class
from api.models.TutorOrganization import TutorOrganization
from api.models.Tutor import Tutor
from django.utils.timezone import now
class TutorSession(models.Model):


  class Meta:
    app_label = 'api'
  #OPTIONAL 1-M with Tutor
  tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, blank=True, null=True)
  #MANDATORY 1-M with TutorOrganization
  tutOrg = models.ForeignKey(TutorOrganization, on_delete=models.CASCADE, blank=False, null=False)
  #MANDATORY 1-1 relation with Class
  classID = models.OneToOneField(Class, on_delete=models.CASCADE, blank=False, null=False)
  tutorSessID = models.PositiveSmallIntegerField(primary_key=True)
  date = models.DateTimeField(default=now)
