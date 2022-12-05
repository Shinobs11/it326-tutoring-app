from api.classes.User import CUser
from api.models.User import User
from api.models.TutorOrgManager import TutorOrgManager
from api.classes.TutorSession import CTutorSession
from api.classes.TutorOrganization import CTutorOrganization
from api.models.TutorOrgManager import TutorOrgManager
from api.models.TutorOrganization import TutorOrganization
class CTutorOrgManager(CUser):
    __tutorOrgManagerID: int
    def __init__(self, tomID: int) -> None:
        self.__tutorOrgManagerID = tomID

    def createTutorOrganization(request):
        TOM =TutorOrgManager.objects.filter(pk='7e5b1e7f-9ca5-499d-804a-e545a0116be5')# tutor org manager object
        name=request.POST['Name']
        instance=TutorOrganization.objects.create(tutOrgName=name) 
        pass

    def createTutorSession(self, TutorOrganization) -> CTutorSession:
        print("Tutor session created.")
        pass
    
    def assignTutor(self,Tutor, TutorSession):
        TutorSession.register()
        pass

        # Checks if email is a tutorOrgMan
    def tutorOrgManEmailCheck(eml):
        item = User.objects.get(email_address=eml)
        item = TutorOrgManager.objects.filter(user=item)
        # If empty...
        if not item:
            return True
        else:
            return False