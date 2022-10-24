from backend.backend.Class import Class

class ClassResources:
    __classData: str
    def __init__(self, classData: str) -> None:
        self.__classData = classData

    def sendClassInfo(self, data: str) -> Class:
        print("Passed resources to Class obj")

    def saveClassResource(self, data: str) -> None:
        print("Saved resources ")