from rest_framework import serializers
from api.models.Student import Student
from api.serializers.UserSerializer import UserSerializer


class StudentSerializer(serializers.ModelSerializer):

  user = UserSerializer(read_only=True)

  class Meta:
    model = Student
    # fields = ['studentID', 'yearInSchool']
    fields = ['user', 'yearInSchool']