from rest_framework import serializers
from api.models.Tutor import Tutor
class TutorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tutor
    fields = ['tutorID']