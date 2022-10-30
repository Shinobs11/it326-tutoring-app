from django.db import models
from api.models import Class, TutorOrganization, Tutor
import datetime
class TutorSession:
    #OPTIONAL 1-M with Tutor
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, blank=True, null=True)
    #MANDATORY 1-M with TutorOrganization
    tutOrg = models.ForeignKey(TutorOrganization, on_delete=models.CASCADE, blank=False, null=False)
    #MANDATORY 1-1 relation with Class
    classID = models.OneToOneField(Class, on_delete=models.CASCADE, blank=False, null=False)
    tutorSessID = models.PositiveSmallIntegerField(primary_key=True)
    date = models.DateTimeField(default=datetime.now)
