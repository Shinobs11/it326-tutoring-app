from django.db import models
from api.models import Class


class ClassResources:
    #OPTIONAL 1-M with Class
    classID = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True, null=True)
    resourceID = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=False)
