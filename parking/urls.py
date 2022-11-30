from django.urls import path

from . import views

urlpatterns = [
    path('in', views.vehicle_in, name='vehicle_in'),  
    path('out', views.vehicle_out, name='vehicle_out'), 
]