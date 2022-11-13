from rest_framework import serializers
from api.models.Tutor import Tutor
class TutorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tutor
    fields = ['user', 'tutorID', 'rating','tutor_subj','Num_Tut_Orgs']