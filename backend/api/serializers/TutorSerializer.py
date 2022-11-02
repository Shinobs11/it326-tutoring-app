from rest_framework import serializers
from api.models.Tutor import Tutor
class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tutor
    fields = ['user', 'tutorID', 'rationg','tutor_subj','Num_Tut_Orgs']