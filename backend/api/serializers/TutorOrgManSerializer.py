from rest_framework import serializers
from api.models.TutorOrgManager import TutorOrgManager


class TutorOrgManSerializer(serializers.ModelSerializer):
  class Meta:
    model = TutorOrgManager
    fields = ['tutOrgManID']