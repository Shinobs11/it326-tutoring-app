from django.db import models
from api.models.TutorSession import TutorSession
from api.models.Student import Student
from django.core.validators import MaxValueValidator, MinValueValidator
class Review:

    class Meta:
        app_label = 'api'

    #PK
    ratingID = models.PositiveSmallIntegerField(primary_key=True)
    #MANDATORY 1-1 with Student
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    #Optional comment section
    #comment = models.CharField(blank=True, null=True)
    #Ratings from 0 to 5
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    # OPTIONAL 1-M relation with TutorSession
    tutSess = models.ForeignKey(TutorSession, on_delete=models.CASCADE, blank=True, null=True)