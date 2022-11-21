from rest_framework import serializers
from api.models.User import User
from api.models.Student import Student
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['uid', 'first_name', 'last_name', 'email_address', 'phone_number', 'student', 'tutor', 'tutorOrgManager']


 