import uuid
from django.db import models
from api.fields import FullNameField, DesiredNameField, EmailAddressField, FirstNameField, LastNameField, PhoneNumberField
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
  uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True,)
  #primary_key=True: uses this field as the primary key for all rows in the User table
  #default=uuid.uuid4: uses this callable/value as the default value for the uid field
  #editable=False: field is not mutatable
  #unique=True: ensures all uid values are unique
  #db_index=True: kinda hard to explain, improves db read performance at the cost of write speed and storage
  #as a rule of thumb, use it for PKs and FKs
  #it can be used in other fields, but definitely be careful with it outside of PKs and FKs otherwise its wasted performance
  
  first_name = FirstNameField(editable=True, blank=False, null=False)
  last_name = LastNameField(editable=True, blank=False, null=False)
  email_address = EmailAddressField(editable=True, blank=False, null=False)
  phone_number = PhoneNumberField(editable=True, blank=False, null=False)
  #Allows 4 choices for what year the user is
  #year = models.CharField(max_length=2, editable=True, blank=False, null=False, choices=yearChoices)
  #blank=False: The field cannot be empty, this is distinct from null in that empty could be something like an empty string
  #null=False: The field cannot be null, more self explanatory, the field cannot have a value of null




