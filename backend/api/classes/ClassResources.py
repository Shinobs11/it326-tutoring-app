#Don't import class: created circular import
class ClassResources:
    __classData: list
    def __init__(self )-> None:
        pass

    def sendClassInfo(self) -> list:
        print("Passed resources to Class obj")
        return self.__classData

    def saveClassResource(self, data: str) -> None:
        self.__classData.append(data)
        print("Saved resources ")
        
    