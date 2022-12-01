from django.http import HttpResponse
from vehicles.models import Vehicles_Brands, Vehicles_Models, Vehicles

import json

def index(request):
    return HttpResponse("Hello, world. You're at the vehicles index.")

# Brands-----------------------------------------
def brand_post(request):
    vehicle_brand = json.loads(request.body)
    return Vehicles_Brands.post_a_brand(vehicle_brand)

def brand_put(request, query_vehicle_brand):
    vehicle_brand = json.loads(request.body)
    return Vehicles_Brands.put_a_brand(vehicle_brand, query_vehicle_brand)

def brand_get(request, query_vehicle_brand):
    return Vehicles_Brands.get_a_brand(query_vehicle_brand)

def brand_delete(request, query_vehicle_brand):
    return Vehicles_Brands.delete_a_brand(query_vehicle_brand)
#-----------------------------------------------
# Models----------------------------------------
def model_post(request):
    vehicle_model = json.loads(request.body)
    return Vehicles_Models.post_a_vehicle_model(vehicle_model)

def model_put(request, query_vehicle_model):
    vehicle_model = json.loads(request.body)
    return Vehicles_Models.put_a_vehicle_model(vehicle_model, query_vehicle_model)

def model_get(request, query_vehicle_model):
    return Vehicles_Models.get_a_vehicle_model(query_vehicle_model)

def model_delete(request, query_vehicle_model):
    return Vehicles_Models.delete_a_vehicle_model(query_vehicle_model)
#------------------------------------------------
# Vehicles---------------------------------------
def vehicle_post(request):
    vehicle = json.loads(request.body)
    return Vehicles.post_a_vehicle(vehicle)

def vehicle_put(request, query_vehicle):
    vehicle = json.loads(request.body)
    return Vehicles.put_a_vehicle(vehicle, query_vehicle)

def vehicle_get(request, query_vehicle):
    return Vehicles.get_a_vehicle(query_vehicle)

def vehicle_delete(request, query_vehicle):
    return Vehicles.delete_a_vehicle(query_vehicle)
#-------------------------------------------------
    
                        