from rest_framework import serializers
from api.models.TutorOrgManager import TutorOrgManager
from api.serializers.UserSerializer import UserSerializer

class TutorOrgManSerializer(serializers.ModelSerializer):

  user = UserSerializer(read_only=True)

  class Meta:
    model = TutorOrgManager
    # fields = ['tutOrgManID']
    fields = ['user']
