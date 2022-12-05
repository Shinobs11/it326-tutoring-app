from api.classes.Student import CStudent
from api.classes.Class import CClass
from api.classes.Observable import CObservable
from api.models.TutorSession import TutorSession
class CTutorSession(CObservable): #Inherits from Observable
    __tutorSessID: int
    __date: str
    __time: float
    __location: str
    __numOfStudents: int
    __numOfTutors: int
    __tutorSessAttendee: CStudent
    __content: str # Whenever a session subjet changes, this is updated to retain the current subject

    # Default Constructor
    def __init__(self):
        pass

    def getClassInfo(self, classObj: CClass) ->str:
        print("Got class info")
        return CClass.getClassInfo()

    def getNumOfAttendees(self) ->int:
        print("Got # of attendees")
        return 0

    def getNumOfTutors(self)->int:
        print("Got # of tutors")
        return 0

    def compareSession(self, other) -> bool:
        print("Comparing both objs....")
        return False

    # Register a user into the subject
    def register(self, user):
        self.user_list.append(user)
        print(user, " was registered")

    # Unregister a user from the subject
    def unregister(self, user):
        self.user_list.remove(user)
        print(user, " was unregistered")

    # Notify all the users in the subject the updated content
    def notifyAll(self):
        for user in self.user_list:
            user.update(self.__content)

    #TODO FIX THIS, Doesn't work
    #Checks if session by that name exists
    def getSess(session):
        item = TutorSession.objects.all().filter(sessName=session)
        if not item:
            return False
        else:
            return True
