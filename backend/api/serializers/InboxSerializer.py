from rest_framework import serializers
from api.models.Inbox import Inbox


class InboxSerializer(serializers.ModelSerializer):
  class Meta:
    model = Inbox
    fields = ['user']
