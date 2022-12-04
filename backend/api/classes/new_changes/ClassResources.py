# The Class Resources File
class ClassResources():
    # Local Variables
    classData = []

    # Constructor
    def __init__(self, resource):
        self.classData.append(resource)

    def getClassResource(self):
        return self.classData

    def addClassResource(self, resource):
        self.classData.append(resource)
        return self.classData