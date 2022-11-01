from django.db import models
from api.models.User import User
from backend.api.models.TutorOrganization import TutorOrganization
from backend.api.models.TutorSession import TutorSession
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
  rating = models.IntegerField(default=0) #may be a better field to allow for decimals
  tutor_subj= models.CharField(max_length=30)
  Num_Tut_Orgs= models.IntegerField(default=0)
  


