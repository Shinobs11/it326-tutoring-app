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
      # Gets the values
      TutOrg = CTutorOrganization.getTutorOrg(request.POST['name'])
      Ddate= request.POST['date']
      sessname = request.POST['SessName']

      # Checks if the inputs were valid
      if ( (TutOrg and Ddate and sessname) and 
           (Ddate[:4].isnumeric() and
            Ddate[5:7].isnumeric() and
            Ddate[9:10].isnumeric() and
            len(Ddate) >= 15)):
        TutSes = TutorSession.objects.create(date=Ddate,sessName=sessname)
        TutOrg.tutSess = TutSes
        TutOrg.save()
        TutSes.save()
        return render(request,'tutorOrghome.html',{})
      else:
        # Display error message back to user
        return render(request, 'SessionCreation.html', {'msg': "Invalid fields, please try again"})

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
      print("WOOHOO")
      return render(request, 'insertResource.html', {})
    else:
      return render(request, 'insertResource.html', {})