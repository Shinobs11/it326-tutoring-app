from django import forms
from .models.TutorOrganization import TutorOrganization

class TutorOrgForm(forms.ModelForm):
    class Meta:
        model=TutorOrganization
        fields = ['tutor','tutOrgMan','tutOrgName']