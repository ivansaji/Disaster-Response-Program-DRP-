from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

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
    return HttpResponse("Find Volunteers")

def findref(request):
    #code to find refugee
    return HttpResponse("Find Refugee")