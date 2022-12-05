from abc import ABC, abstractmethod
from api.models.User import User as UserDB
from django.shortcuts import render, redirect

# need to pull in user database: should be in form
# from .models import Stock
from api.models import User
class CUser(ABC):
    name: str
    userID: str
    password: str
    phoneNo: str
    email: str
   #@abstractmethod
    def __init__(self, name:str, UID:str, password:str, phoneNumber: str, email: str):
        self.name=name
        self.userID=UID
        self.password=password
        self.phoneNo=phoneNumber
        self.email=email
            
    

    #Checks if email is already taken
    def authenticate(eml):
        item = User.objects.all().filter(email_address=eml)
        if not item:
            return False
    def login(email,paswrd):
        if CUser.authenticate(email,paswrd)==True:
            return True #Plug in html when ready
        else:
            return False

            

    def checkpassword(psw1,psw2):
        if psw1==psw2:
            return True
        else:
            return False

    def register(fn,ln,eml,phn,pswd,pswd2):
        pass
        
        

    #@abstractmethod
    def update(self, content): # Updates
        pass