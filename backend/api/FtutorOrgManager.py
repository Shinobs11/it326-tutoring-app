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
from api.classes.TutorSession import CTutorSession
from api.classes.User import CUser
from api.models.TutorSession import TutorSession as DB_TutorSession
from api.models.User import User as DB_User
from api.classes.TutorOrgManager import CTutorOrgManager
#from api.forms import TutorOrgForm
  
class FtutorOrgManager():
    
    def tutorOrgMgrhome(request):
        alltutorgs=TutorOrganization.objects.all
        print(alltutorgs)
        return render(request, 'tutOrgMgrhome.html',{'tutorgs':alltutorgs}) 

    def removeUserPath(request):
        return render(request, 'deleteUser.html', {})

    #TODO Add functionality to check if session is under user's account
    def removeUser(request):
        if request.method == "POST":
            email = request.POST['email']
            session = request.POST['name']
            if CTutorSession.getSess(session):
                return render(request, 'deleteUser.html', {'msg': "Not a session!"})
            if not CUser.registerEmailCheck(email):
                return render(request, 'deleteUser.html', {'msg': "Email not in database"})
            sess = DB_TutorSession.object.filter(sessName=session)
            user = DB_User.object.filter(email=email)
            sess.student.remove(user)
        else:
            return render(request, 'deleteUser.html', {'msg': "Enter info"})

    def createTutorOrg(request):
        if request.method=="POST":
            CTutorOrganization.createTutorOrganization(request)
            alltutorgs=TutorOrganization.objects.all
            #fill in parameters later
            # need to create tutor before able to finish
            return render(request,'tutOrgMgrhome.html',{'tutorgs':alltutorgs})
        
        return render(request,'TutorOrgCreation.html',{})
        #TutorOrgManager= TutorOrgManager.objects.create(tutOrgManID=random.randint(0,99999999))
        