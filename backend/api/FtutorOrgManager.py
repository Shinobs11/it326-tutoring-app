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
from api.models.TutorOrgManager import *
from api.models.TutorOrganization import TutorOrganization
from .forms import TutorOrgForm
  
class FtutorOrgManager():
    
    def tutorOrgMgrhome(request):
        return render(request, 'tutorhome.html',{}) 

    def createTutorOrg(request):
        if request.method=="POST":
            form = TutorOrgForm(request.POST or None)
            ID=random.randint(0,99999999999)
            TOM =TutorOrgManager.objects.get(pk='1515a87f-41f0-46ae-83bd-72ba99dc2b4a')# tutor org manager object
            name=request.POST['Name']
            TutorOrganization.objects.create(tutOrgMan=TOM,tutOrgName=name)
            #fill in parameters later
            # need to create tutor before able to finish
            return render(request,'tutorOrghome.html',{})
        
        return render(request,'TutorOrgCreation.html',{})
        #TutorOrgManager= TutorOrgManager.objects.create(tutOrgManID=random.randint(0,99999999))
        