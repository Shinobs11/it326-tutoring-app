from rest_framework import serializers
from api.models.Class import Class


class ClassSerializer(serializers.ModelSerializer):
  class Meta:
    model = Class
    fields = ['className', 'classDescription']