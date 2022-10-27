from abc import ABC, abstractmethod
class User(ABC):
    __name: str
    __userID: str
    __password: str
    __phoneNo: str
    __email: str
    @abstractmethod
    def __init__(self, name:str, UID:str, password:str, phoneNumber: str, email: str):
        self.__name=name
        self.__userID=UID
        self.__password=password
        self.__phoneNo=phoneNumber
        self.__email=email
    @abstractmethod
    def login(self,UID,paswrd):
        pass
    @abstractmethod
    def autheticate(self):
        pass