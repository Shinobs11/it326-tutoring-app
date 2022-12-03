# The Class Resources File
class ClassResources():
    # Local Variables
    classData: str

    # Constructor
    def __init__(self, resource):
        self.classData = resource

    def saveClassResource(self, resource):
        self.classData = resource
        return self.classData