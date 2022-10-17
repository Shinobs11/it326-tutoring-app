from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['uid', 'first_name', 'last_name', 'email_address', 'phone_number'] 