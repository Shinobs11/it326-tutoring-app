from api.classes.User import User
from api.classes.TutorSession import TutorSession
from api.classes.TutorOrganization import TutorOrganization
class TutorOrgManager(User):
    __tutorOrgManagerID: int
    def __init__(self, tomID: int) -> None:
        self.__tutorOrgManagerID = tomID

    def createTutorOrganization(self) -> TutorOrganization:
        print("Tutor Organization created.")
        return TutorOrganization()

    def createTutorSession(self, TutorOrganization) -> TutorSession:
        print("Tutor session created.")
        pass
    
    def assignTutor(self,Tutor, TutorSession):
        TutorSession.register()
        pass
      

