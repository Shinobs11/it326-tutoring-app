try:
  from api.factories.UserFactory import UserFactory
  from api.factories.StudentFactory import StudentFactory
  from api.factories.TutorFactory import TutorFactory
  from api.factories.TutorOrgManagerFactory import TutorOrgManagerFactory

except ImportError:
  from .UserFactory import UserFactory
  from .StudentFactory import StudentFactory
  from .TutorFactory import TutorFactory
  from .TutorOrgManagerFactory import TutorOrgManagerFactory

