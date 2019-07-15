from django.shortcuts import render,redirect
from django.utils import timezone

from .models import Refugee,Volunteer
from .forms import RefugeeRegistration,VolunteerRegistration

# Create your views here.
def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RefugeeRegistration(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            info = form.save(commit=False)
            info.pub_time = timezone.now()
            info.save()

            # ...
            # redirect to a new URL:
            return redirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RefugeeRegistration()
        context =  {'form': form}

    return render(request, 'index.html',context)
