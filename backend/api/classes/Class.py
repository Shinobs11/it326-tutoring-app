import string
from api.classes.ClassResources import ClassResources as CR

class Class:
    __classID: int
    __className: string
    __classType: string
    __studentsEnrolled: int
    #__ClassReso: ClassResouce-- Will just declare in constructor for sake of ease
    # Default Constructor
    def __init__(self, id, name, type, numStudents):
        self.__classID = id
        self.__className = name
        self.__classType = type
        self.__studentsEnrolled = numStudents
        self.__Resource=CR.classResources()
        
    # Gets the Class Info
    def createClassResources(self, data:str):
        self.__Resource.saveClassResource(data)
        
    def getClassInfo(self) ->list:
        return self.__Resource.sendClassInfo()
    