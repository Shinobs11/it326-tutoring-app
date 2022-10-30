from django.db import models
from api.models import TutorOrgManager, Tutor


class TutorOrganization:
    tutOrgID = models.PositiveSmallIntegerField(primary_key=True)
    #MANDATORY M-M relation with Tutor
    tutor = models.ManyToManyField(Tutor, blank=False, null=False)
    # MANDATORY M-M relation with TutorOrgManager
    tutOrgMan = models.ManyToManyField(TutorOrgManager, blank=False, null=False)
    tutOrgName = models.CharField(unique=True, max_length=30)