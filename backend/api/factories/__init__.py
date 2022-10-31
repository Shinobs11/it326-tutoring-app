try:
	from api.factories.UserFactory import UserFactory
	from api.factories.StudentFactory import StudentFactory

except ImportError:
	from .UserFactory import UserFactory
	from .StudentFactory import StudentFactory
