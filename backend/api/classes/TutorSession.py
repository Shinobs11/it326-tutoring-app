from Student import Student
from Tutor import Tutor
from Class import Class

class TutorSession:
    __tutorSessID: int
    __date: str
    __time: str #changed to string
    __location: str
    __numOfStudents: int
    __numOfTutors: int
    __tutorSessAttendee: Student # should be a list
    __tutorSessTutor: Tutor
    def __init__(self,date,time,location):
        self.__tutorSessID=0 #Need to find way to initalize ID
        self.__date=date
        self.__time=time
        self.__location=location
        self.__numOfStudents=0
        self.__numOfTutors=0
        self.fun=12
        
    def getClassInfo(self, classObj: Class) ->list:#returns a list of strings
        print("Got class info")
        return classObj.getClassInfo()

    def getNumOfAttendees(self) ->int:
        print("Got # of attendees")
        return self.__numOfStudents

    def getNumOfTutors(self)->int:
        print("Got # of tutors")
        return self.__numOfTutors
    
    def getDate(self)->str:
        return self.__date
    
    def getTime(self)->str:
        return self.__time
    
    def compareSession(self, tutSess) -> bool: #Need to look into how to send a class its own data type. May need to mannualy input value error
        #Return true if both objects are during the same time
        #Return false if tutorsessions are at different times
        print("Comparing both objs....")
        if(self.__date==tutSess.getDate() and self.__time==tutSess.getTime()):
            return True
        else:
            return False
    
    def AddStudent(self,stuObj:Student):
        self.__numOfStudents+=1
        self.__tutorSessAttendee.append(stuObj)
        
        
    
    def AddTutor(self,tutObj):
        self.__numOfTutors+=1
        self.__tutorSessTutor.append(tutObj)