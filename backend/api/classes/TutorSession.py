from api.classes.Student import Student
from api.classes.Class import Class
from api.classes.Observable import Observable

class TutorSession(Observable): #Inherits from Observable
    __tutorSessID: int
    __date: str
    __time: float
    __location: str
    __numOfStudents: int
    __numOfTutors: int
    __tutorSessAttendee: Student
    __content: str # Whenever a session subjet changes, this is updated to retain the current subject

    # Default Constructor
    def __init__(self):
        pass

    def getClassInfo(self, classObj: Class) ->str:
        print("Got class info")
        return ""

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
    @Override
    def notifyAll(self):
        for user in self.user_list:
            user.update(self.__content)
