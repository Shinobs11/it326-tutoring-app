from http.client import HTTPResponse
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
from api.classes.TutorOrgManager import CTutorOrgManager
from api.classes.Tutor import CTutor
from api.models.Review import Review
from api.classes.Review import CReview
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
      tutorsess= TutorOrgManager.objects.get()
      return render(request, 'tutorsession.html',{'tutorsession':tutorsess})

  def ratePage(request):
    return render(request, 'reviewTutor.html',{})

  def registerSessPage(request):
    TS=TutorSession.objects.all()#TS is for tutorsessions
    return render(request, 'registerSession.html',{'tutsess':TS})


  @staticmethod
  def rate(request):
    if request.method =='POST':
      email = request.POST['email']
      session = request.POST['session']
      rating = request.POST['rating']
      #Checks if email is in DB
      if not CUser.registerEmailCheck(email):
        return render(request, 'registerSession.html', {'msg': "Email not in DB"})
      #Checks if email is of a student
      if CStudent.studentEmailCheck(email):
        return render(request, 'reviewTutor.html', {'msg': "Not a student email!"})
      #Checks if session exists
      if not CTutorSession.getSess(session):
        return render(request, 'reviewTutor.html', {'msg': "Not a session!"})
      if not CReview.checkRating(rating):
        return render(request, 'reviewTutor.html', {'msg': "Invalid input"})
      if CStudent.isStudentinSession(email,session):
        return render(request, 'reviewTutor.html', {'msg': "Not in session"})
      if CReview.ifRatingExists(email,session):
        return render(request, 'reviewTutor.html', {'msg': "Review already filed with this tutor session"})
      stu = CUser.getStudent(email)
      sess = DB_TutorSession.objects.get(sessName=session)
      Review.objects.create(student=stu, rating=rating,tutSess=sess)
      
      return render(request, 'studenthome.html', {'msg': "Review sent"})

    else:
      return render(request, 'reviewTutor.html', {'msg': "Enter info"})


  def registerStudentSess(request):
    if request.method == 'POST':
      email = request.POST['email']
      session = request.POST['name']
      if not CUser.registerEmailCheck(email):
        return render(request, 'registerSession.html', {'msg': "Not your email!"})
        #CHecks if a student or not
      if CStudent.studentEmailCheck(email):
        return render(request, 'registerSession.html', {'msg': "Not a student email!"})
      if not CTutorSession.getSess(session):
        return render(request, 'registerSession.html', {'msg': "Not a session!"})
      sess = DB_TutorSession.objects.get(sessName=session)
      stu = CUser.getStudent(email)
      sess.student.add(stu)
      sess.save()
      return render(request, 'studenthome.html', {'msg': "Enrolled"})
    else:
      return render(request, 'registerSession.html', {'msg': "Enter info"})

  def unenrollSession(request):
    if request.method == 'POST':
      # Get the user inputs
      email = request.POST['stuEmail']
      sess = request.POST['sessName']

      if not CUser.registerEmailCheck(email):
        return render(request, 'unenrollSession.html', {'msg': "Not your email!"})
        #CHecks if a student or not
      if CStudent.studentEmailCheck(email):
        return render(request, 'unenrollSession.html', {'msg': "Not a student email!"})
      if not CTutorSession.getSess(sess):
        return render(request, 'unenrollSession.html', {'msg': "Not a session!"})

      sess = DB_TutorSession.objects.get(sessName=sess)
      stu = CUser.getStudent(email)
      sess.student.remove(stu)
      sess.save()


      return render(request, "homebase.html", {'msg': "Unenrolled from the session!"})
    else:
      return render(request, "unenrollSession.html", {})