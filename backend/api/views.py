from django.shortcuts import render
from api.models.User import User
from api.models.Student import Student
from api.serializers.StudentSerializer import StudentSerializer
from api.serializers.UserSerializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
# Create your views here.


#https://www.django-rest-framework.org/tutorial/3-class-based-views/ going based off of this for now
class UserList(
  mixins.ListModelMixin,
  mixins.CreateModelMixin,
  generics.GenericAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

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

class StudentList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
      return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
      return self.create(request, *args, **kwargs)

class StudentDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
      return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
      return self.delete(request, *args, **kwargs)

  