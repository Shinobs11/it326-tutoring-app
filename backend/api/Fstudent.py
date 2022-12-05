from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from api.models.Class import Class
from api.FtutorSess import *
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from api.models.TutorOrgManager import TutorOrgManager
from api.classes.User import CUser
from api.classes.Student import CStudent
from api.classes.Review import CReview
from api.classes.TutorSession import CTutorSession
from api.models.TutorSession import TutorSession as DB_TutorSession
from api.classes.Student import CStudent
from api.models.Review import Review
from api.models.TutorSession import TutorSession



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
    TS=TutorSession.objects.all()#TS is for tutorsessions
    return render(request, 'registerSession.html',{'tutsess':TS})

  #TODO Fix email check, fix session check (check only sessions in user's account)
  #TODO Check if email is a Student email
  #TODO Drop-down menu for tutor sessions?
  # TODO Change getUser to getStudent
  #TODO Allow same student to make multiple reviews
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
      sess = DB_TutorSession.objects.get(sessName=session)
      Review.objects.create(student=stu, rating=rating,tutSess=sess)
      return render(request, 'studenthome.html', {'msg': "Review sent"})

    else:
      return render(request, 'reviewTutor.html', {'msg': "Enter info"})

    #TODO Check for already enrolled users
    #TODO Make sure user is a student/tutor
    #TODO Test edge cases
  def registerSess(request):
    if request.method == 'POST':
      email = request.POST['email']
      session = request.POST['name']
      if not CUser.registerEmailCheck(email):
        return render(request, 'registerSession.html', {'msg': "Not your email!"})
      if not CTutorSession.getSess(session):
        return render(request, 'registerSession.html', {'msg': "Not a session!"})
      sess = DB_TutorSession.objects.get(sessName=session)
      stu = CUser.getUser(email)
      sess.student.add(stu)
      sess.save()
      return render(request, 'studenthome.html', {'msg': "Enrolled"})
    else:
      return render(request, 'registerSession.html', {'msg': "Enter info"})
