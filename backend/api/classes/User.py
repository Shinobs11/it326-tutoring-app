from abc import ABC, abstractmethod
from api.models.User import User as UserDB
from django.shortcuts import render, redirect
# need to pull in user database: should be in form
# from .models import Stock
from api.models import User
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
            

    def authenticate(self,user_id,passattempt):
        # TODO: Get the database table
        # to pull from user
        item= User.objects.get(pk=user_id)
        if passattempt==item.password:
            return True
        else:
            return False

        while (foundUser != True):
            # Search the elements
            foundUser = True
            
    def login(self,UID,paswrd):
        if self.authenticate(UID,paswrd)==True:
            return redirect('something.html',{}) #Plug in html when ready
        else:
            return redirect('samepage.html',{'message',"retrypass"})# plug in right html file


    def register(self):
        pass
        

    @abstractmethod
    def update(self, content): # Updates
        pass