from abc import ABC, abstractmethod
from api.models.User import User as UserDB
# need to pull in user database: should be in form
# from .models import Stock
from models import user
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
        # TODO: Get the database table
        # to pull from user
        item= user.objects.get(pk=user_id)
        foundUser = False

        while (foundUser != True):
            # Search the elements
            foundUser = True

    def register(self):
        pass

    @abstractmethod
    def update(self, content): # Updates
        pass