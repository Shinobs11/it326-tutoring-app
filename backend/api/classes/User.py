from abc import ABC, abstractmethod
from api.models.User import User as UserDB
from django.shortcuts import render, redirect

# need to pull in user database: should be in form
# from .models import Stock
from api.models.Student import Student
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

    # Checks if email is already taken
    def registerEmailCheck(eml):
        item = User.objects.all().filter(email_address=eml)
        if not item:
            return False
        else:
            return True
    def authenticate(eml,passattempt):
        # TODO: Get the database table
        item= User.objects.get(email_address=eml)
        if passattempt==item.password:
            return True
        
    def login(email,paswrd):
        if CUser.authenticate(email,paswrd)==True:
            return True #Plug in html when ready
        else:
            return False

    def checkpassword(pswd,psw2):
        if(pswd==psw2):
            return True
        else:
            return False

    def getUser(email):
        item = User.objects.get(email_address=email)
        item = item.student
        return item


    def getTutOrgMgr(email):
        item = User.objects.get(email_address=email)
        item=item.tutorOrgManager
        return item