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
from api.models.TutorOrgManager import TutorOrgManager
#from api.forms import TutorOrgForm
  
class FtutorOrgManager():
    
    def tutorOrgMgrhome(request):
        alltutorgs=TutorOrganization.objects.all
        return render(request, 'tutOrgMgrhome.html',{'tutorgs':alltutorgs}) 

    def removeUserPath(request):
        return render(request, 'deleteUser.html', {})

    def tutorOrgPath(request):
        return render(request, 'TutorOrgCreation.html', {})

    #TODO Add functionality to check if that user is registered under that session
    #TODO Check that user is a student/tutor (to remove)
    def removeUser(request):
        if request.method == "POST":
            email = request.POST['email']
            session = request.POST['name']
            #Checks if session exists
            if not CTutorSession.getSess(session):
                return render(request, 'deleteUser.html', {'msg': "Not a session!"})
            #Checks if user exists via email
            if not CUser.registerEmailCheck(email):
                return render(request, 'deleteUser.html', {'msg': "Email not in database"})
            sess = DB_TutorSession.objects.get(sessName=session)
            user = CUser.getStudent(email)
            sess.student.remove(user)
            sess.save()
            return render(request,'tutOrgMgrhome.html',{'msg': "Removed user"})
        else:
            return render(request, 'deleteUser.html', {'msg': "Enter info"})

    #TODO Add other values (tutors, tutor sess)
    # TODO Check if email is a TutOrgMan email
    #TODO Change getUser to getTutOrgMan
    def createTutorOrg(request):
        if request.method == "POST":
            email = request.POST['email']
            name = request.POST['name']
            if not CUser.registerEmailCheck(email):
                return render(request, 'TutorOrgCreation.html', {'msg': "Wrong email!"})
            tutOrgMa = TutorOrgManager.objects.get(user=User.objects.get(email_address=email))
            instance=TutorOrganization.objects.create(tutOrgName=name)
            instance.tutOrgMan.add(tutOrgMa)
            instance.save()
            
            all=TutorOrganization.objects.all()
            
            return render(request,'tutOrgMgrhome.html',{'tutorgs':all})
        else:
            return render(request,'TutorOrgCreation.html',{})
        #TutorOrgManager= TutorOrgManager.objects.create(tutOrgManID=random.randint(0,99999999))
        