from django.db import models
#dear god i didn't think this would be THIS difficult https://www.w3.org/International/questions/qa-personal-names
# TODOS: Make validators for fields, especially Email field for local part of the address


class FirstNameField(models.fields.CharField):
  description: str = "First name of user"
  
  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 50
    super().__init__(*args, **kwargs)

class LastNameField(models.fields.CharField):
  description: str = "Last name of user"

  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 50
    super().__init__(*args, **kwargs)

class FullNameField(models.fields.CharField):
  description: str = "Full name of user"

  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 255
    super().__init__(*args, **kwargs)

class DesiredNameField(models.fields.CharField):
  description: str = "Desired name of user(What they would like to be identified by)"

  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 255
    super().__init__(*args, **kwargs)


# this is also stupidly difficult to figure out constraints for
class EmailAddressField(models.fields.CharField):
  description: str = "Email address"

  def __init__(self, *args, **kwargs):
    kwargs['max_length']=254
    super().__init__(*args, **kwargs)

class PhoneNumberField(models.fields.CharField):
  description: str = "Phone number"

  def __init__(self, *args, **kwargs):
    kwargs['max_length']=254
    super().__init__(*args, **kwargs)


class PasswordField(models.fields.CharField):
  description: str = "password"

  def __init__(self, *args, **kwargs):
    kwargs['max_length'] = 254
    super().__init__(*args, **kwargs)