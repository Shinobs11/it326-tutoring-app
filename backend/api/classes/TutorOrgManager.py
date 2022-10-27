from backend.backend import TutorOrganization, User, TutorSession

class TutorOrgManager(User):
    __tutorOrgManagerID: int
    def __init__(self, tomID: int) -> None:
        self.__tutorOrgManagerID = tomID

    def createTutorOrganization(self) -> TutorOrganization:
        print("Tutor Organization created.")

    def creeateTutorSession(self, TutorOrganization) -> TutorSession:
        print("Tutor session created.")

