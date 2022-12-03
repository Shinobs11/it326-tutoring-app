from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render


class Fuser():
  
  def login(request):
    # need to add authenticate once entered in information in login area
    # getting intial page layout completed
    return render(request,'login.html',{})
  
  def userhome(request):
    return render(request,'homeuser.html',{})
  
  