from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from api.models import Student


class Class:
    #OPTIONAL 1-M relation with Student
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)

    #PK, Only class IDs b/w 100-999 are allowed
    classID = models.PositiveSmallIntegerField(primary_key=True,
    validators=[MaxValueValidator(999), MinValueValidator(100)], blank=False)

    resourceType = models.CharField(max_length=15, blank=True)