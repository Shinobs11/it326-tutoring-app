# The Class File
from ClassResources import ClassResources as CR

class Class:
    # Local Variables
    className: str
    classType: str
    studentsEnrolled: int
    classResource: CR # The Class Resource Object
    

    # Constructor
    def init(self, name, type, resource):
        self.className = name
        self.classType = type
        self.studentsEnrolled = 0 # NOTE: Set to 0 because when we create a class, there should be no one enrolled yet
        self.classResource = CR(resource)
    
    # Calls ClassResources to send the class info NOTE: Assuming this is returning the class data
    def getClassInfo(self) -> str:
        return self.classResource.classData

    # Updates the Class Resource's classData str
    def updateClassInfo(self, data:str):
        return self.classResource.saveClassResource(data)