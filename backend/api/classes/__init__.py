try:
	from api.classes.Tutor import Tutor
	from api.classes.TutorSession import TutorSession
	from api.classes.User import User
	from api.classes.Student import Student
	from api.classes.Class import Class
	from api.classes.TutorOrgManager import TutorOrgManager
	from api.classes.TutorOrganization import TutorOrganization
	from api.classes.ClassResources import ClassResources

except ImportError:
	from .Tutor import Tutor
	from .TutorSession import TutorSession
	from .User import User
	from .Student import Student
	from .Class import Class
	from .TutorOrgManager import TutorOrgManager
	from .TutorOrganization import TutorOrganization
	from .ClassResources import ClassResources
