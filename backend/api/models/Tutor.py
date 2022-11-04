from django.db import models
from api.models.User import User
class Tutor(models.Model):

  class Meta:
    app_label = 'api'


  # OPTIONAL 1-1 relation with User
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  #0-* relation with TutorSessions
  #0-* relation with TutorOrganizaiton
  tutorID = models.PositiveSmallIntegerField(primary_key=True)
  rating = models.FloatField(default=0)
  tutor_subj= models.CharField(max_length=30)
  Num_Tut_Orgs= models.PositiveSmallIntegerField(default=0)
  


