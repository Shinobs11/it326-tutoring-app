from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from api.models.TutorSession import TutorSession
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render
import random
from api.models.TutorSession import TutorSession
from api.classes.TutorOrganization  import CTutorOrganization
from api.classes.TutorSession import CTutorSession
#from api.classes.TutorOrganization import *

  
class FtutorOrg():
  
  def tutorOrghome(request):
    return render(request, 'tutorOrghome.html',{})
  
  def createSession(request):    
    if request.method =="POST":
      Organization=request.POST['name']
      sessionName=request.POST['SessName']
      if not CTutorOrganization.getOrg(Organization):
        return render(request, 'SessionCreation.html', {'msg': "Not an Organization!"})
      if not CTutorSession.getSess(sessionName):
        pass
      else:
        return render(request, 'SessionCreation.html', {'msg': "Name already taken!"})
      TutOrg=CTutorOrganization.getTutorOrg(request.POST['name'])
      Ddate= (request.POST['date'])
      sessname=request.POST['SessName'] 
      TutSes=TutorSession.objects.create(tutorSessID=SessionID,date=Ddate,sessName=sessname)
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
        print("DELETING IT", sessname)
        return render(request, 'tutorOrghome.html', {'msg': "Session successfully deleted!"})
      else:
        return render(request, 'removeSession.html', {'msg': "Session not found. Please try again"})
    else:
      return render(request, 'removeSession.html', {})
  
  def insertResource(request):
    if request.method == "POST":
      sessname = CTutorSession.getTutorSession(request.POST['sessName'])

      if (sessname):
        # Create an instance of the class resource
        classData = request.POST['classData']
        resourceID = 0
        for resources in SessionResource.object.all():
          resourceID = resourceID + 1

        #SessionResource.object.create(sessionID = )
        print(classData)
        print(resourceID)
        return render(request, 'tutorOrghome.html', {'msg': "Class Resource successfully inserted!"})

      return render(request, 'insertResource.html', {})
    else:
      return render(request, 'insertResource.html', {})