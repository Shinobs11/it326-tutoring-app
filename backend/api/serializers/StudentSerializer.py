from rest_framework import serializers
from api.models.Student import Student


class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['user', 'studentID', 'tutorSessHours']