from django.db import models
from api.models.User import User
from api.models.TutorSession import TutorSession

class Student(models.Model):

  class Meta:
    app_label = 'api'

    """ Currently inside of User but thinking would be a better fit for student 
    yearChoices = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior')
  ] """

  #OPTIONAL 1-1 relation with User
  user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
  #PK
  studentID = models.PositiveSmallIntegerField(primary_key=True, blank=False, null=False)
  tutorSessionID= models.foreignKey(TutorSession, on_delete=models.CASCADE,blank=True, null=True)
  tutorSessHours= models.PositiveSmallIntegerField(default=0)



