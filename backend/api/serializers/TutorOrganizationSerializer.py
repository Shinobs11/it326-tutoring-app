from rest_framework import serializers
from api.models.TutorOrganization import TutorOrganization
from api.serializers.UserSerializer import UserSerializer


class TutorOrganizationSerializer(serializers.ModelSerializer):
  class Meta:
    model = TutorOrganization
    fields = ['tutOrgID','tutor', 'tutOrgMan', 'tutOrgName','tutOrgDescription']
