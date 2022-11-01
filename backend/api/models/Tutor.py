from django.db import models
from api.models.User import User
from api.models.TutorOrganization import TutorOrganization
from api.models.TutorSession import TutorSession
class Tutor(models.Model):

  class Meta:
    app_label = 'api'


  # OPTIONAL 1-1 relation with User
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
  #0-* relation with TutorSessions
  tutorSessionID= models.foreignKey(TutorSession, on_delete=models.CASCADE,blank=True, null=True)
  #0-* relation with TutorOrganizaiton
  tutorOrganizationID= models.foreignKey(TutorOrganization, on_delete=models.CASCADE, blank=True, null=True)
  
  tutorID = models.PositiveSmallIntegerField(primary_key=True)
  rating = models.FloatField(default=0)
  tutor_subj= models.CharField(max_length=30)
  Num_Tut_Orgs= models.PositiveSmallIntegerField(default=0)
  


