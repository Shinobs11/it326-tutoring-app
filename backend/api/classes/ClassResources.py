from api.classes.Class import Class

class ClassResources:
    __classData: str
    def __init__(self, classData: str) -> None:
        self.__classData = classData

    def sendClassInfo(self, data: str) -> Class:
        print("Passed resources to Class obj")
        return Class()

    def saveClassResource(self, data: str) -> None:
        print("Saved resources ")