from rest_framework import serializers
from api.models.SessionResource import SessionResource


class SessionResourceSerializer(serializers.ModelSerializer):
  class Meta:
    model = SessionResource
    fields = ['sessionID','resourceID', 'name', 'content']
    # depth=1