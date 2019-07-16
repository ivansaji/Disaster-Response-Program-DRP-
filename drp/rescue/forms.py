from django import forms
from .models import Refugee,Volunteer

class RefugeeRegistration(forms.ModelForm):
    class Meta:
        model = Refugee
        fields ={'name','contact','location'}

class VolunteerRegistration(forms.ModelForm):
    class Meta:
        model = Volunteer
        fields ={'name','contact','location'}

