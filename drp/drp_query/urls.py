from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('volreg', views.volreg, name='volreg'),
    path('refreg', views.refreg, name='refreg'),
    path('findvol', views.findvol, name='findvol'),
    path('findref', views.findref, name='findref'),
]
