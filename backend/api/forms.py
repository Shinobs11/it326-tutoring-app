from django import forms 
from .models import TutorSession
from .models import TutorOrganization

class TutorSessionForm(forms.ModelForm):
    class Meta:
        model = TutorSession
        fields = ['tutOrg','classID','tutorSessID','date','location','rate']
        
class TutorOrgForm(forms.ModelForm):
    class Meta:
        model = TutorOrganization
        fields =['tutOrgMan','tutOrgName']
