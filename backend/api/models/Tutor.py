from django.db import models
from api.models.User import User
class Tutor(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    primary_key=True
  )
  test_field = models.PositiveSmallIntegerField(null=True, blank=True, default=32)
