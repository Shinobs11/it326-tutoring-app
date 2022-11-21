from rest_framework import serializers
from api.models.Student import Student
from api.serializers.UserSerializer import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['studentID', 'yearInSchool']