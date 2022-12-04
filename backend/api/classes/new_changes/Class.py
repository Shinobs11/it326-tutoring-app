# The Class File
from classes.new_changes.ClassResources import ClassResources as CR

class Class():
    # Local Variables
    className: str
    classType: str
    classResource: CR # The Class Resource Object
    

    # Constructor
    def __init__(self, name, type):
        self.className = name
        self.classType = type
    
    # Calls ClassResources to send the class info NOTE: Assuming this is returning the class data
    def getClassData(self) -> str:
        return self.classResource.getClassResource()

    # Updates the Class Resource's classData str
    def addClassResource(self, data:str):
        return self.classResource.saveClassResource(data)