from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render
from api.classes.User import CUser
from api.classes.Tutor import CTutor
from api.models.TutorOrgManager import TutorOrgManager
from api.classes.UserFactory import UserFactory

class Fuser():
  
  def login(request):
    if request.method=='POST':
      email=request.POST['email']
      pswd=request.POST['password']
      if not CUser.registerEmailCheck(email):
        return render(request, 'login.html', {'message': "Email not in database"})
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

  def searchForTutorPath(request):
    return render(request,'searchTutor.html',{})


  def searchTutor(request):
    if request.method == 'POST':
      email = request.POST['email']
      if not CUser.registerEmailCheck(email):
        return render(request, 'searchTutor.html', {'msg': "Email not in database"})
      if CTutor.tutorEmailCheck(email):
        return render(request, 'searchTutor.html', {'msg': "Not a tutor email"})
      item = User.objects.get(email_address=email)
      return render(request, 'searchTutor.html', {'item': item})
    else:
      return render(request, 'searchTutor.html', {'msg': "Enter info"})


  def createProfile(request):
    if request.method=='POST':
      first=request.POST['Fname']
      last=request.POST['Lname']
      email=request.POST['email']
      phone=request.POST['Phone Number']
      pswd=request.POST['password']
      pswd2=request.POST['password']
      type=request.POST['usertype']
      if CUser.registerEmailCheck(email):
        return render(request, 'login.html', {'msg': "Email already taken"})
      elif CUser.checkpassword(pswd,pswd2):
        # Have the user factory create an object of the User type
        UserFactory.buildUser(first,last,email,phone,pswd,type)
        return render(request,'homeuser.html',{})
      else:
        return render(request,'login.html',{'msg':"Passwords do not match"})
        
      
    else:
      return render(request,'createProfile.html',{})


  def deleteProfilePath(request):
    return render(request,'deleteProfile.html',{})



  def deleteProfile(request):
    if request.method=='POST':
      email=request.POST['email']
      password=request.POST['password']
      if not CUser.authenticate(email,password):
        return render(request, 'deleteProfile.html', {'msg': 'Wrong password'})
      UserFactory.deleteUser(request)
      return render(request,'login.html',{'messagedelete':'Successfully Deleted'})

    else:
      return render(request, 'deleteProfile.html', {'msg': 'Input data'})