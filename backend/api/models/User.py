import uuid
from django.db import models
from api.fields import EmailAddressField, FirstNameField, LastNameField, PhoneNumberField
# Create your models here.


class User(models.Model):

  class Meta:
    app_label = 'api'

  yearChoices = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior')
  ]
  uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
  first_name = FirstNameField(editable=True, blank=False, null=False)
  last_name = LastNameField(editable=True, blank=False, null=False)
  email_address = EmailAddressField(editable=True, blank=False, null=False)
  phone_number = PhoneNumberField(editable=True, blank=False, null=False)
  #year = models.CharField(max_length=2, editable=True, blank=False, null=False, choices=yearChoices)







