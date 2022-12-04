from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render
from api.classes.User import CUser



class Fuser():
  
  def login(request):
    if request.method=='POST':
      email=request.POST['email']
      pswd=request.POST['password']
      if CUser.login(email,pswd)==True:
        return render(request,'homeuser.html',{})
      else:
        return render(request,'login.html',{'message':"incorrect login Try again"})
      
    # need to add authenticate once entered in information in login area
    # getting intial page layout completed
    return render(request,'login.html',{})
  
  def userhome(request):
    return render(request,'homeuser.html',{})
  
  def searchtutorsession(request):
    return render(request,'' ,{})
  
  def createProfile(request):
    if request.method=='POST' and request.POST['name']==None:
      first=request.POST['Fname']
      last=request.POST['Lname']
      email=request.POST['email']
      phone=request.POST['PhoneNumber']
      pswd=request.POST['password']
      pswd2=request.POST['password']
      if User.checkpassword(pswd,pswd2):
        User.register(first,last,email,phone,pswd,pswd2)
      else:
        render(request,'login.html',{'message2':"Incorrect Password"})
        
      
      render(request, )
    else:
      return render(request,'createProfile.html',{})
  
  