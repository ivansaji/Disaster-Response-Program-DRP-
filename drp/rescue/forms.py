from django import forms
from .models import Refugee,Volunteer

class RefugeeRegistration(forms.ModelForm):
    class Meta:
        model = Refugee
        fields ={'name','contact','location','threat_rating','necessities'}

class VolunteerRegistration(forms.ModelForm):
    class Meta:
        model = Refugee
        fields ={'name','contact','location'}

