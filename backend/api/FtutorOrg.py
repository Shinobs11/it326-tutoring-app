from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from api.models.TutorSession import TutorSession
from api.models.TutorSession import TutorSession
from api.models.SessionResource import SessionResource
from api.models.Class import Class
from api.classes.User import CUser
from api.classes.TutorOrganization  import CTutorOrganization
from api.classes.TutorSession import CTutorSession
from api.classes.Tutor import CTutor
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render
import random

#from api.classes.TutorOrganization import *

class FtutorOrg():
  
  def tutorOrghome(request):
    return render(request, 'tutorOrghome.html',{})
  
  def createSession(request):    
    if request.method =="POST":
      Organization=request.POST['name']
      sessionName=request.POST['SessName']
      Ddate= (request.POST['date'])

      # Make sure the inputs are valid
      if not CTutorOrganization.getOrg(Organization):
        return render(request, 'SessionCreation.html', {'msg': "Not an Organization!"})
      if not CTutorSession.getSess(sessionName):
        pass
      else:
        return render(request, 'SessionCreation.html', {'msg': "Name already taken!"})
      if (len(Ddate) == 0):
        return render(request, 'SessionCreation.html', {'msg': "Please enter a date"})
      
      # If valid, we go to create the session and add it to the database
      TutOrg=CTutorOrganization.getTutorOrg(request.POST['name'])
      TutSes=TutorSession.objects.create(date=Ddate,sessName=sessionName)
      TutOrg.tutSess=TutSes
      TutOrg.save()
      TutSes.save()
      return render(request,'tutorOrghome.html',{})
      
    else:
      return render(request,'SessionCreation.html',{})
    
  def removeSession(request):
    if request.method =="POST":
      # Get the values
      sessname = CTutorSession.getTutorSession(request.POST['SessName'])

      # Make sure the name was found
      if (sessname):
        TutorSession.objects.filter(sessName=sessname).delete()
        return render(request, 'tutorOrghome.html', {'msg': "Session successfully deleted!"})
      else:
        return render(request, 'removeSession.html', {'msg': "Session not found. Please try again"})
    else:
      return render(request, 'removeSession.html', {})
  
  def insertResource(request):
    if request.method == "POST":
      className = request.POST['className']
      classData = request.POST['classData']
      sessname = CTutorSession.getTutorSession(request.POST['sessName'])

      # Check if the session exists
      if not CTutorSession.getSess(sessname):
        return render(request, 'insertResource.html', {'msg': "Session does not exist!"})
      
      # Get the session
      session = TutorSession.objects.get(sessName=sessname)
        
      # Add the class resource to the DB
      classResource = SessionResource.objects.create(sessionID = session, name = className, content = classData)
      classResource.save()
          
      return render(request, 'tutorOrghome.html', {'msg': "Class Resource successfully inserted!"})
    else:
      return render(request, 'insertResource.html', {})

  def addClasstoSession(request):
    if request.method == "POST":
      name = request.POST['className']
      desc = request.POST['classDesc']
      session = CTutorSession.getTutorSession(request.POST['sessName'])

      # Check if the session exists
      if not CTutorSession.getSess(session):
        return render(request, 'addClassToSession.html', {'msg': "Session does not exist!"})
      
      # Add Tutor To Session
      sess = TutorSession.objects.get(sessName = session)
      theClass = Class.objects.create(className = name, classDescription = desc)
      sess.classID.add(theClass)

      sess.save()
      theClass.save()
      
      return render(request, 'tutorOrghome.html', {'msg': "Class successfully added!"})
    else:
      return render(request, 'addClassToSession.html', {})
    
  def addTutorToSession(request):
    if request.method == "POST":
      tutEmail = request.POST['tutorEmail']
      session = request.POST['sessName']

      # Check if the email is valid
      if (CTutor.tutorEmailCheck(tutEmail)):
        return render(request, 'addTutorToSession.html', {'msg': "Email provided does not belong to a tutor"})
      
      # Check if the session exists
      if not CTutorSession.getSess(session):
        return render(request, 'addTutorToSession.html', {'msg': "Session does not exist!"})

      # Add Tutor To Session
      sess = TutorSession.objects.get(sessName = session)
      tutor = CUser.getTutor(tutEmail)
      sess.tutor.add(tutor)
      sess.save()

      return render(request, 'tutorOrghome.html', {'msg': "Tutor successfully added!"})
    else:
      return render(request, 'addTutorToSession.html', {})

