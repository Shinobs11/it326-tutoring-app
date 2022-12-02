from django.db import models
from api.models.Student import Student
from api.models.TutorOrganization import TutorOrganization

class Rate(models.Model):
    
    class Meta:
        app_label= 'api'
        
    #optional 1-M relation with Student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    tutorOrg= models.ForeignKey(TutorOrganization, on_delete=models.CASCADE, blank=True, null=True)


