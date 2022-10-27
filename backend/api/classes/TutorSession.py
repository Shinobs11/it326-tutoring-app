from api.classes.Student import Student
from api.classes.Class import Class

class TutorSession:
    __tutorSessID: int
    __date: str
    __time: float
    __location: str
    __numOfStudents: int
    __numOfTutors: int
    __tutorSessAttendee: Student
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