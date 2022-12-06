from api.classes.Student import CStudent
from api.classes.Class import CClass
from api.classes.Observable import CObservable
from api.models.TutorSession import TutorSession
from api.models.Student import Student
from api.models.User import User
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

    #Checks if session by that name exists
    def getTutorSession(name):
        if (TutorSession.objects.filter(sessName=name)):
            return name

    #Checks if student is in a given tutor session
    #TODO Fix this
    def studentInSess(email, session):
        item = User.objects.get(email_address=email)
        item = item.student
        item = TutorSession.objects.filter(sessName=session,student=item)
        #If they are not in session, return False
        if not item:
            return False
        else:
            return True

    def tutorInSess(email, session):
        item = User.objects.get(email_address=email)
        item = item.tutor
        item = TutorSession.objects.filter(sessName=session,tutor=item)
        #If they are not in session, return False
        if not item:
            return False
        else:
            return True