from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from api.serializers.TutorSerializer import TutorSerializer
from api.models.TutorOrgManager import TutorOrgManager
from api.serializers.TutorOrgManSerializer import TutorOrgManSerializer
from api.serializers.StudentSerializer import StudentSerializer
from api.serializers.UserSerializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render
# Create your views here.


#https://www.django-rest-framework.org/tutorial/3-class-based-views/ going based off of this for now
class UserList(
  mixins.ListModelMixin,
  mixins.CreateModelMixin,
  generics.GenericAPIView):
  # List of all the objects
  queryset = User.objects.all()

  # Formats the users in json
  serializer_class = UserSerializer

  # Gets all the users from the database
  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  # Create a new user object
  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)

class UserDetail(
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  generics.GenericAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.delete(request, *args, **kwargs)

class StudentList(UserList):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentDetail(UserDetail):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TutorList(UserList):
  queryset = Tutor.objects.all()
  serializer_class = TutorSerializer

class TutorDetail(UserDetail):
  queryset = Tutor.objects.all()
  serializer_class = TutorSerializer

class TutorOrgManList(UserList):
  queryset = TutorOrgManager.objects.all()
  serializer_class = TutorOrgManSerializer

class TutorOrgManDetail(UserDetail):
  queryset = TutorOrgManager.objects.all()
  serializer_class = TutorOrgManSerializer


class user():
  
  def login(request):
    # need to add authenticate once entered in information in login area
    # getting intial page layout completed
    return render(request,'login.html',{})
  
  def userhome(request):
    return render(request,'homeuser.html',{})

#File tutor, nameing convention to keep seperate from other classes
class Fstudent():
  #will send person to student homepage
  def studenthome(request):
    return render(request, 'studenthome.html',{})

class Ftutor():
  #will send person to student homepage
  def tutorhome(request):
    return render(request, 'tutorhome.html',{}) 