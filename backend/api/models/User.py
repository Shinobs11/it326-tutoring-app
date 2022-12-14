import uuid
from django.db import models
from api.fields import FullNameField, DesiredNameField, EmailAddressField, FirstNameField, LastNameField, PhoneNumberField
from api.fields.fields import PasswordField
# from api.models.Student import Student
# from api.models.Tutor import Tutor
# from api.models.TutorOrgManager import TutorOrgManager
# Create your models here.


class User(models.Model):

  class Meta:
    app_label = 'api'


  uid = models.UUIDField(primary_key=True, default=uuid.uuid4 ,editable=False, unique=True, db_index=True, null=False, blank=False)

  first_name = FirstNameField(editable=True, blank=False, null=False)
  last_name = LastNameField(editable=True, blank=False, null=False)
  email_address = EmailAddressField(editable=True, blank=False, null=False)
  phone_number = PhoneNumberField(editable=True, blank=False, null=False)
  password = PasswordField(max_length=100, default="J=genius")




