from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Volunteer,Refugee

def index(request):
    return HttpResponse("Hey Ivan")

def volreg(request):
    #code for volunteer register
    return HttpResponse("Volunteer Register")

def refreg(request):
    #code for Refugee Register
    return HttpResponse("Refugee Register")

def findvol(request):
    #code for find volunteer
    latest_data = Volunteer.objects.order_by('location')[:5]
    context = {'latest_data': latest_data}
    return render(request, 'drp/index.html', context)

def findref(request):
    #code to find refugee
    latest_data = Refugee.objects.order_by('location')[:5]
    context = {'latest_data': latest_data}
    return render(request, 'drp/index.html', context)