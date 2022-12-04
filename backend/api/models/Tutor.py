from django.db import models

import uuid
class Tutor(models.Model):

  class Meta:
    app_label = 'api'


  
  #0-* relation with TutorSessions
  #0-* relation with TutorOrganizaiton
  tutorID = models.UUIDField(primary_key=True,default=uuid.uuid4 ,editable=False, unique=True, db_index=True, null=False, blank=False)
  # rating = models.FloatField(default=0)
  # tutor_subj= models.CharField(max_length=30)
  # Num_Tut_Orgs= models.PositiveSmallIntegerField(default=0)
  


