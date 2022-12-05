from rest_framework import serializers
from api.models.TutorSession import TutorSession
from api.serializers.UserSerializer import UserSerializer


class TutorSessionSerializer(serializers.ModelSerializer):
  class Meta:
    model = TutorSession
    fields = ['tutor', 'student', 'classID', 'tutorSessID', 'date','sessName','location']