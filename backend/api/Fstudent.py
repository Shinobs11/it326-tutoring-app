from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from api.models.Class import Class
from api.FtutorSess import *
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render
from api.models.TutorOrgManager import TutorOrgManager
from api.classes.User import CUser
from api.classes.Student import CStudent
from api.classes.Review import CReview
from api.classes.TutorSession import CTutorSession
from api.classes.Student import CStudent
from api.models.Review import Review


#The F stands for File. Will make code much easier to read through
#File tutor, nameing convention to keep seperate from other classes
class Fstudent():
  #will send person to student homepage
  def studenthome(request):
    return render(request, 'studenthome.html',{})
  
  def showtutorSessions(request):# will create seperate method for searching for specific criteria
    import json
    if request.method== 'POST':
      #if the button is pushed get
      pass
    else:
      tutorsess= TutorOrgManager.objects.get(pk='1515a87f-41f0-46ae-83bd-72ba99dc2b4a')
      return render(request, 'tutorsession.html',{'tutorsession':tutorsess})
  def registerTutorSession(request):
    pass

  def rate(request):
    pass

  def ratePage(request):
    return render(request, 'reviewTutor.html',{})

  def registerSessPage(request):
    return render(request, 'registerSession.html',{})

  #TODO Fix email check, fix session check (check only sessions in user's account)
  #TODO Check if email is a Student email
  #TODO Drop-down menu for tutor sessions?
  # TODO Change getUser to getStudent
  def rate(request):
    if request.method =='POST':
      email = request.POST['email']
      session = request.POST['session']
      rating = request.POST['rating']
      if not CUser.registerEmailCheck(email):
        return render(request, 'reviewTutor.html', {'msg': "Not your email!"})
      if not CTutorSession.getSess(session):
        return render(request, 'reviewTutor.html', {'msg': "Not a session!"})
      if not CReview.checkRating(rating):
        return render(request, 'reviewTutor.html', {'msg': "Invalid input"})
      stu = CUser.getUser(email)
      #TODO Fix this issue
      Review.objects.create(student="866f9db6-a29d-451c-a846-da924a996196", rating=rating,tutSess=session)
      return render(request, 'studenthome.html', {'msg': "Review sent"})

    else:
      return render(request, 'reviewTutor.html', {'msg': "Enter info"})

    #TODO
  def registerSess(request):
    pass
