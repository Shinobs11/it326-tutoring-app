from django.db import models
from api.models.TutorSession import TutorSession
from api.models.Student import Student
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
class Review(models.Model):

    class Meta:
        app_label = 'api'

    #PK
    ratingID = models.UUIDField(primary_key=True, default=uuid.uuid4)
    #MANDATORY 1-1 with Student
    student = models.OneToOneField(Student, on_delete=models.DO_NOTHING, unique=False)
    #Optional comment section
    #comment = models.CharField(blank=True, null=True)
    #Ratings from 0 to 5
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    # OPTIONAL 1-M relation with TutorSession
    tutSess = models.ForeignKey(TutorSession, on_delete=models.DO_NOTHING, blank=True, null=True)