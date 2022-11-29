from django.http import HttpResponse
from vehicles.models import Vehicles_Brands, Vehicles_Types, Vehicles_Models, Vehicles

import json

def index(request):
    return HttpResponse("Hello, world. You're at the vehicles index.")

# Brands-----------------------------------------
def brand_post(request):
    vehicle_brand = json.loads(request.body)
    return HttpResponse(Vehicles_Brands.post_a_brand(vehicle_brand))

def brand_put(request, query_vehicle_brand):
    vehicle_brand = json.loads(request.body)
    return HttpResponse(Vehicles_Brands.put_a_brand(vehicle_brand, query_vehicle_brand))

def brand_get(request, query_vehicle_brand):
    return HttpResponse(Vehicles_Brands.get_a_brand(query_vehicle_brand))

def brand_delete(request, query_vehicle_brand):
    return HttpResponse(Vehicles_Brands.delete_a_brand(query_vehicle_brand))
#-----------------------------------------------
# Types-----------------------------------------
def type_post(request):
    vehicle_type = json.loads(request.body)
    return HttpResponse(Vehicles_Types.post_a_vehicle_type(vehicle_type))

def type_put(request, query_vehicle_type):
    vehicle_type= json.loads(request.body)
    return HttpResponse(Vehicles_Types.put_a_vehicle_type(vehicle_type, query_vehicle_type))

def type_get(request, query_vehicle_type):
    return HttpResponse(Vehicles_Types.get_a_vehicle_type(query_vehicle_type))

def type_delete(request, query_vehicle_type):
    return HttpResponse(Vehicles_Types.delete_a_type(query_vehicle_type))
#-----------------------------------------------
# Models----------------------------------------
def model_post(request):
    vehicle_model = json.loads(request.body)
    return HttpResponse(Vehicles_Models.post_a_vehicle_model(vehicle_model))

def model_put(request, query_vehicle_model):
    vehicle_model = json.loads(request.body)
    return HttpResponse(Vehicles_Models.put_a_vehicle_model(vehicle_model, query_vehicle_model))

def model_get(request, query_vehicle_model):
    return HttpResponse(Vehicles_Models.get_a_vehicle_model(query_vehicle_model))

def model_delete(request, query_vehicle_model):
    return HttpResponse(Vehicles_Models.delete_a_vehicle_model(query_vehicle_model))
#------------------------------------------------
# Vehicles---------------------------------------
def vehicle_post(request):
    vehicle = json.loads(request.body)
    return HttpResponse(Vehicles.post_a_vehicle(vehicle))

def vehicle_put(request, query_vehicle):
    vehicle = json.loads(request.body)
    return HttpResponse(Vehicles.put_a_vehicle(vehicle, query_vehicle))

def vehicle_get(request, query_vehicle):
    return HttpResponse(Vehicles.get_a_vehicle(query_vehicle))

def vehicle_delete(request, query_vehicle):
    return HttpResponse(Vehicles.delete_a_vehicle(query_vehicle))
#-------------------------------------------------
    
                        