from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from api.models.TutorSession import TutorSession
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render
from .forms import TutorSessionForm
import random
from api.classes.TutorOrganization import *

  
class FtutorOrg():
  
  def tutorOrghome(request):
    return render(request, 'tutorOrghome.html',{})
  
  def createSession(request):
    #creating session ID here
    sessionID= FtutorOrg.createID()
    
    if request.method =="POST":
      form = TutorSessionForm(request.POST or None)
      DtutOrgID= None
      DclassID=request.POST['classID']
      DtutorSessID=sessionID
      Ddate= request.POST['date']
      Drate= '0'
      TutorSession.objects.create(tutOrgID=DtutOrgID,classID=DclassID,tutorSessID=DtutorSessID,date=Ddate,rate=Drate)        
      return render(request,'tutorOrghome.html',{})
      
    else:
      return render(request,'SessionCreation.html',{'ID':sessionID})
    
  def createID(): # can probably come up with a better way for ID creation but this will work for now
    return random.randint(0,999999999)