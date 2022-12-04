try:
	from api.classes.Tutor import CTutor
	from api.classes.TutorSession import CTutorSession
	from api.classes.User import CUser
	from api.classes.Student import CStudent
	from api.classes.Class import CClass
	from api.classes.TutorOrgManager import CTutorOrgManager
	from api.classes.TutorOrganization import TutorOrganization
	from api.classes.ClassResources import CClassResources

except ImportError:
	from .Tutor import CTutor
	from .TutorSession import CTutorSession
	from .User import CUser
	from .Student import CStudent
	from .Class import CClass
	from .TutorOrgManager import CTutorOrgManager
	from .TutorOrganization import CTutorOrganization
	from .ClassResources import CClassResources
