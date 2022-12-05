from rest_framework import serializers
from api.models.Tutor import Tutor
from api.serializers.UserSerializer import UserSerializer
class TutorSerializer(serializers.ModelSerializer):

  user = UserSerializer(read_only=True)

  class Meta:
    model = Tutor
    # fields = ['tutorID']
    fields = ['user']