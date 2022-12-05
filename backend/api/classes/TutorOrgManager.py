from api.classes.User import CUser
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
      

