from api.classes.User import CUser
from api.classes.TutorSession import CTutorSession
from api.classes.TutorOrganization import CTutorOrganization
class CTutorOrgManager(CUser):
    __tutorOrgManagerID: int
    def __init__(self, tomID: int) -> None:
        self.__tutorOrgManagerID = tomID

    def createTutorOrganization(self) -> CTutorOrganization:
        print("Tutor Organization created.")
        return CTutorOrganization()

    def createTutorSession(self, TutorOrganization) -> CTutorSession:
        print("Tutor session created.")
        pass
    
    def assignTutor(self,Tutor, TutorSession):
        TutorSession.register()
        pass
      

