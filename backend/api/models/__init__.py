try:
	from api.models.Tutor import Tutor
	from api.models.TutorSession import TutorSession
	from api.models.User import User
	from api.models.Student import Student
	from api.models.Class import Class
	from api.models.TutorOrgManager import TutorOrgManager
	from api.models.TutorOrganization import TutorOrganization
	from backend.api.models.SessionResources import ClassResources

except ImportError:
	from .Tutor import Tutor
	from .TutorSession import TutorSession
	from .User import User
	from .Student import Student
	from .Class import Class
	from .TutorOrgManager import TutorOrgManager
	from .TutorOrganization import TutorOrganization
	from .SessionResources import ClassResources
