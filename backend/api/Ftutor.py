from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from api.classes.User import CUser
from api.classes.TutorSession import CTutorSession
from api.classes.Student import CStudent
from api.models.TutorSession import TutorSession as DB_TutorSession
from api.classes.TutorOrgManager import CTutorOrgManager
from api.classes.Tutor import CTutor
from api.models.TutorSession import TutorSession
from api.models.TutorOrganization import TutorOrganization 
from api.classes.TutorOrganization import CTutorOrganization

class Ftutor():
  #will send person to student homepage
  def tutorhome(request):
    return render(request, 'tutorhome.html',{})

  def registerTutorSessPage(request):
    TS=TutorSession.objects.all()#TS is for tutorsessions
    return render(request, 'registerSessTutor.html', {'tutsess':TS})

  #Register tutor for session
  def registerTutorSess(request):
    if request.method == 'POST':
      email = request.POST['email']
      session = request.POST['name']
      if not CUser.registerEmailCheck(email):
        return render(request, 'registerSessTutor.html', {'msg': "Email not in Database"})
        #Checks if tutor email
      if CTutor.tutorEmailCheck(email):
        return render(request, 'registerSessTutor.html', {'msg': "Not a tutor email!"})
      if not CTutorSession.getSess(session):
        return render(request, 'registerSessTutor.html', {'msg': "Not a session!"})
      if CTutor.isTutorInOrganization(email,session):
        return render(request, 'registerSessTutor.html', {'msg': "Not in this tutor organization!"})
      sess = DB_TutorSession.objects.get(sessName=session)
      tut = CUser.getTutor(email)
      sess.tutor.add(tut)
      sess.save()
      return render(request, 'tutorhome.html', {'msg': "Enrolled"})
    else:
      return render(request, 'registerSessTutor.html', {'msg': "Enter info"})
    
  def registerTutorOrgPage(request):
    TS=TutorOrganization.objects.all#TS is for tutorsessions
    return render(request, 'registerTutOrgTutor.html', {'tuts':TS})
  
  def registerOrgtut(request):
    if request.method == 'POST':
      email = request.POST['email']
      Organization = request.POST['name']
      if not CUser.registerEmailCheck(email):
        return render(request, 'registerTutOrgTutor.html', {'msg': "Email not in Database"})
        #Checks if tutor email
      if CTutor.tutorEmailCheck(email):
        return render(request, 'registerTutOrgTutor.html', {'msg': "Not a tutor email!"})
      if not CTutorOrganization.getOrg(Organization):
        return render(request, 'registerTutOrgTutor.html', {'msg': "Not an Organization!"})
      Org = TutorOrganization.objects.get(tutOrgName=Organization)
      tut = CUser.getTutor(email)
      Org.tutor.add(tut)
      Org.save()
      return render(request, 'tutorhome.html', {'msg': "Enrolled"})
    else:
      return render(request, 'registerSessTutor.html', {'msg': "Enter info"})

  def unregisterFromOrg(request):
    if request.method == 'POST':
      email = request.POST['email']
      Organization = request.POST['name']
      if not CUser.registerEmailCheck(email):
        return render(request, 'registerTutOrgTutor.html', {'msg': "Email not in Database"})
        #Checks if tutor email
      if CTutor.tutorEmailCheck(email):
        return render(request, 'registerTutOrgTutor.html', {'msg': "Not a tutor email!"})
      if not CTutorOrganization.getOrg(Organization):
        return render(request, 'registerTutOrgTutor.html', {'msg': "Not an Organization!"})
      Org = TutorOrganization.objects.get(tutOrgName=Organization)
      tut = CUser.getTutor(email)
      Org.tutor.remove(tut)
      Org.save()
      return render(request, 'tutorhome.html', {'msg': "Unregistered from Tutor Org!"})
    else:
      return render(request, 'unregisterFromOrg.html', {})