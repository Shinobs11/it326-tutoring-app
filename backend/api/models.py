import uuid
from django.db import models
from api.fields import FullNameField, DesiredNameField, EmailAddressField, FirstNameField, LastNameField, PhoneNumberField
# Create your models here.


class User(models.Model):

  
  uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True,)
  #primary_key=True: uses this field as the primary key for all rows in the User table
  #default=uuid.uuid4: uses this callable/value as the default value for the uid field
  #editable=False: field is not mutatable
  #unique=True: ensures all uid values are unique
  #db_index=True: kinda hard to explain, improves db read performance at the cost of write speed and storage
  #as a rule of thumb, use it for PKs and FKs
  #it can be used in other fields, but definitely be careful with it outside of PKs and FKs otherwise its wasted performance
  
  first_name = FirstNameField(editable=True, blank=False, null=False)
  #blank=False: The field cannot be empty, this is distinct from null in that empty could be something like an empty string
  #null=False: The field cannot be null, more self explanatory, the field cannot have a value of null

  last_name = LastNameField(editable=True, blank=False, null=False)
  email_address = EmailAddressField(editable=True, blank=False, null=False)
  phone_number = PhoneNumberField(editable=True, blank=False, null=False)


class Student(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    primary_key=True
  )
  test_field = models.PositiveSmallIntegerField(null=True, blank=True, default=32)

class Tutor(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    primary_key=True
  )
  test_field = models.PositiveSmallIntegerField(null=True, blank=True, default=32)

class TutorOrgManager(models.Model):
  user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    primary_key=True
  )
  test_field = models.PositiveSmallIntegerField(null=True, blank=True, default=32)
