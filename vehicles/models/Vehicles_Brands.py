from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from setup.services import post_object, put_object, get_object, delete_object

class Vehicles_Brands(models.Model):
    brand = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    class Meta:
        db_table = 'vehicles_brands';
           
    def post_a_brand(vehicle_brand):
        return post_object(vehicle_brand, Vehicles_Brands)
        
    def put_a_brand(edited_vehicle_brand, query_vehicle_brand):
        return put_object(edited_vehicle_brand, query_vehicle_brand, 'brand', Vehicles_Brands)
        
    def get_a_brand(query_vehicle_brand):
        return get_object(query_vehicle_brand, 'brand', Vehicles_Brands)
    
    def delete_a_brand(query_vehicle_brand):
        return delete_object(query_vehicle_brand, 'brand', Vehicles_Brands)