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


#The F stands for File. Will make code much easier to read through
#File tutor, nameing convention to keep seperate from other classes
class Fstudent():
  #will send person to student homepage
  def studenthome(request):
    return render(request, 'studenthome.html',{})
  
  def showtutorSessions(request):# will create seperate method for searching for specific criteria
    import json
    if request.method== 'POST':
      #if the button is pushed  get
      pass
    else:
      tutorsess= TutorOrgManager.objects.get(pk='1515a87f-41f0-46ae-83bd-72ba99dc2b4a')
      return render(request, 'tutorsession.html',{'tutorsession':tutorsess})
  
  def rate(request):
    pass
    
