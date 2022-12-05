from urllib.request import Request
from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from api.models.Class import Class
from api.models.Review import Review
from api.models.TutorSession import TutorSession
from api.models.TutorOrganization import TutorOrganization
from api.serializers.TutorSerializer import TutorSerializer
from api.models.TutorOrgManager import TutorOrgManager
from api.serializers.TutorOrgManSerializer import TutorOrgManSerializer
from api.serializers.StudentSerializer import StudentSerializer
from api.serializers.UserSerializer import UserSerializer
from api.serializers.ClassSerializer import ClassSerializer
from api.serializers.TutorSessionSerializer import TutorSessionSerializer
from api.serializers.TutorOrganizationSerializer import TutorOrganizationSerializer
from api.serializers.ReviewSerializer import ReviewSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
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

class TutorSessionList(UserList):
    queryset = TutorSession.objects.all()
    serializer_class = TutorSessionSerializer

class TutorSessionDetail(UserDetail):
    queryset = TutorSession.objects.all()
    serializer_class = TutorSessionSerializer

class TutorOrganizationList(UserList):
        queryset = TutorOrganization.objects.all()
        serializer_class = TutorOrganizationSerializer

class TutorOrganizationDetail(UserDetail):
        queryset = TutorOrganization.objects.all()
        serializer_class = TutorOrganizationSerializer

class ClassList(UserList):
        queryset = Class.objects.all()
        serializer_class = ClassSerializer

class ClassDetail(UserDetail):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class Session(APIView):
  def get(self, request, format=None):
    sessions = TutorSession.objects.all()
    serializer = TutorSessionSerializer(sessions, many=True)
    return Response(serializer.data)
  pass


class ReviewList(UserList):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
class ReviewDetail(UserDetail):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

