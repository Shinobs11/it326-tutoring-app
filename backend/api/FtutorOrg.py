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
    #creating session ID here
    SessionID=0
    for i in TutorSession.objects.all():
      SessionID = SessionID+1
    
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
