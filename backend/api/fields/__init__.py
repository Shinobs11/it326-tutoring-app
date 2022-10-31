try:
	from api.fields.fields import FirstNameField
	from api.fields.fields import LastNameField
	from api.fields.fields import FullNameField
	from api.fields.fields import DesiredNameField
	from api.fields.fields import EmailAddressField
	from api.fields.fields import PhoneNumberField

except ImportError:
	from .fields import FirstNameField
	from .fields import LastNameField
	from .fields import FullNameField
	from .fields import DesiredNameField
	from .fields import EmailAddressField
	from .fields import PhoneNumberField
