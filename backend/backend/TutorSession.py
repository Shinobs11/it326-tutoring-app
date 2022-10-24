from backend.backend import Student, Class

class TutorSession:
    __tutorSessID: int
    __date: str
    __time: float
    __location: str
    __numOfStudents: int
    __numOfTutors: int
    __tutorSessAttendee: Student[0]
    def __init__(self):
        pass

    def getClassInfo(self, classObj: Class) ->str:
        print("Got class info")

    def getNumOfAttendees(self) ->int:
        print("Got # of attendees")

    def getNumOfTutors(self)->int:
        print("Got # of tutors")

    def compareSession(self, other) -> bool:
        print("Comparing both objs....")