from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from api.models.TutorSession import TutorSession
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render
import random
from api.models.TutorOrgManager import *
from api.models.TutorOrganization import TutorOrganization
from api.classes.TutorOrganization import CTutorOrganization
#from api.forms import TutorOrgForm
  
class FtutorOrgManager():
    
    def tutorOrgMgrhome(request):
        alltutorgs=TutorOrganization.objects.all
        return render(request, 'tutOrgMgrhome.html',{'tutorgs':alltutorgs}) 

    def createTutorOrg(request):
        if request.method=="POST":
            CTutorOrganization.createTutorOrganization(request)
            alltutorgs=TutorOrganization.objects.all
            #fill in parameters later
            # need to create tutor before able to finish
            return render(request,'tutOrgMgrhome.html',{'tutorgs':alltutorgs})
        
        return render(request,'TutorOrgCreation.html',{})
        #TutorOrgManager= TutorOrgManager.objects.create(tutOrgManID=random.randint(0,99999999))
        