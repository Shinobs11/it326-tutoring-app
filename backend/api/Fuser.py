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
      CUser.login(email,pswd)
      
    # need to add authenticate once entered in information in login area
    # getting intial page layout completed
    return render(request,'login.html',{})
  
  def userhome(request):
    return render(request,'homeuser.html',{})
  
  def searchtutorsession(request):
    return render(request,'' ,{})
  
  