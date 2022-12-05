from rest_framework import serializers
from api.models.Review import Review


class ReviewSerializer(serializers.ModelSerializer):
  class Meta:
    model = Review
    fields = ['ratingID', 'student','rating','tutSess']