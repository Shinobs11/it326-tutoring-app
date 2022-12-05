from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from api.models.TutorSession import TutorSession
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render
from api.models.TutorOrganization import TutorOrganization


class FtutorSession():
    
  def gettutorSession():
    return TutorSession.objects.all
  
  def loadSesPg(request,tutSesID):
    sesObj=TutorSession.objects.get(tutorSessID=tutSesID)
    tutOrgObj=TutorOrganization.objects.get(tutSess=sesObj)
    return render(request, 'tutorSessionPage.html',{'sesInfo':sesObj,'tutorg':tutOrgObj})
    pass
  