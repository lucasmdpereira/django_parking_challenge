from django.http import HttpResponse
from .models import Vehicles_Brands, Vehicles_Types

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

#-----------------------------------------------