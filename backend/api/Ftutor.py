from api.models.User import User
from api.models.Student import Student
from api.models.Tutor import Tutor
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view
from django.shortcuts import render

class Ftutor():
  #will send person to student homepage
  def tutorhome(request):
    return render(request, 'tutorhome.html',{}) 