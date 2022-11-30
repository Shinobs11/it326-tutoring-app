from abc import ABC, abstractmethod
from api.models.User import User as UserDB
class User(ABC):
    name: str
    userID: str
    password: str
    phoneNo: str
    email: str
    @abstractmethod
    def __init__(self, name:str, UID:str, password:str, phoneNumber: str, email: str):
        self.name=name
        self.userID=UID
        self.password=password
        self.phoneNo=phoneNumber
        self.email=email

    def login(self,UID,paswrd):
        pass

    def authenticate(self):
        pass

    def register(self):
        pass

    @abstractmethod
    def update(self, content): # Updates
        pass