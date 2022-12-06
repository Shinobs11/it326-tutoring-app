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
from api.classes.TutorSession import CTutorSession
from api.models.TutorSession import TutorSession

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

  def searchSession(request):
    if request.method == 'POST':
      sess = request.POST['TutSesName']
      if not CTutorSession.SessionCheck(sess):
        return render(request, 'searchSession.html', {'msg': "Tutor Session not in database"})
      item = TutorSession.objects.get(sessName=sess)
      return render(request, 'searchSession.html', {'item': item})
    else:
      return render(request, 'searchSession.html', {'msg': "Enter info"})

  def createProfile(request):
    if request.method=='POST':
      first=request.POST['Fname']
      last=request.POST['Lname']
      email=request.POST['email']
      phone=request.POST['Phone Number']
      pswd=request.POST['password']
      pswd2=request.POST['password2']
      type=request.POST['usertype']
      if CUser.registerEmailCheck(email):
        return render(request, 'login.html', {'msg': "Email already taken"})
      if CUser.checkpassword(pswd,pswd2):
        return render(request, 'login.html', {'msg': "Passwords do not match"})
      #if CUser.typeCheck(type):
      #  return render(request, 'login.html', {'msg': "Not valid UserType"})
      UserFactory.buildUser(first,last,email,phone,pswd,type)
      return render(request,'homeuser.html',{})

    else:
      return render(request,'createProfile.html',{})


  def editProfile(request):
    if request.method == 'POST':
      curEmail = request.POST['curEmail']
      newEmail = request.POST['email']
      newPhone = request.POST['phoneNumber']
      newPass = request.POST['password']
      validate = request.POST['repeat']
      foundUser = False
      # Check if the email and phoneNumber are not already in the DB
      for users in User.objects.all():
        if (users.email_address == curEmail):
          foundUser = True
        if (users.email_address == newEmail):
          return render(request, 'editProfile.html',{'msg': "Email already taken"})
        elif (users.phone_number == newPhone):
          return render(request, 'editProfile.html',{'msg': "Phone Number already taken"})
      
      # Make sure the passwords matched up
      if CUser.checkpassword(newPass,validate):
        return render(request, 'editProfile.html',{'msg': "Phone Number already taken"})

      # Get the entry from the DB
      if (not foundUser):
        return render(request, 'editProfile.html',{'msg': "That email does not exist"})
      
      user = User.objects.get(email_address = curEmail)
      
      # Update the user's fields
      if (len(newEmail) > 0):
        user.email_address = newEmail
      
      if (len(newPhone) > 0):
        user.phone_number = newPhone

      if (len(newPass) > 0):
        user.password = newPass
      
      user.save()

      
      return render(request, 'homebase.html', {'msg': "Profile successfully updated!"})
    else:
      return render(request, 'editProfile.html',{})

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