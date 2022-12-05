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
#from api.classes.TutorOrganization import *

  
class FtutorOrg():
  
  def tutorOrghome(request):
    return render(request, 'tutorOrghome.html',{})
  
  def createSession(request):
    #creating session ID here
    print(TutorSession.objects.all())
    for i in TutorSession.objects.all():
      sessionID+=1
    
    if request.method =="POST":
      DclassID=request.POST['classID']
      DtutorSessID=sessionID
      Ddate= request.POST['date']
      Drate= '0'
      TutorSession.objects.create(tutorSessID=DtutorSessID,date=Ddate)        
      return render(request,'tutorOrghome.html',{})
      
    else:
      return render(request,'SessionCreation.html',{'ID':sessionID})
