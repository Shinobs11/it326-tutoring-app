from abc import ABC, abstractmethod
class User(ABC):
    __name:str
    __userID:int
    __password:int
    __phoneNo:int
    __email:str
    @abstractmethod
    def __init__(self,nm,UID,paswrd,phnNo,eml):
        self.__name=nm
        self.__userID=UID
        self.__password=paswrd
        self.__phoneNo=phnNo
        self.__email=eml
    @abstractmethod
    def login(self,UID,paswrd):
        pass
    @abstractmethod
    def autheticate(self):
        pass