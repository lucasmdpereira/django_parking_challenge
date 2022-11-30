from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.forms.models import model_to_dict

from vehicles.services import standardize_in, standardize_out, check_and_update_object

import json

class Vehicles_Brands(models.Model):
    brand = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    class Meta:
        db_table = 'vehicles_brands';
           
    def post_a_brand(vehicle_brand):
        vehicle_brand = standardize_in(vehicle_brand)
        new_vehicle_brand = Vehicles_Brands(**vehicle_brand)
        try:
            new_vehicle_brand.clean_fields()
            try:
                new_vehicle_brand.save()
                return standardize_out(new_vehicle_brand)
            except:
                return standardize_out({"brand": [f'{list(object.values())[0]} already exists']})
        except ValidationError as e:
            return standardize_out(e.message_dict)
        
    def put_a_brand(edited_vehicle_brand, query_vehicle_brand):
        try:
            vehicle_brand = Vehicles_Brands.objects.get(brand = query_vehicle_brand)
        except:
            return standardize_out({"brand": [f'{query_vehicle_brand} not found']})
        
        vehicle_brand = check_and_update_object(model_to_dict(vehicle_brand), edited_vehicle_brand)
        try: 
            test_vehicle_brand = Vehicles_Brands(**vehicle_brand)
            test_vehicle_brand.clean_fields()
        except ValidationError as e:
            return json.dumps(e.message_dict)
        
        Vehicles_Brands.objects.filter(pk = vehicle_brand['id']).update(**edited_vehicle_brand)
        return standardize_out(vehicle_brand)    

    def get_a_brand(query_vehicle_brand):
        try:
            vehicle_brand = Vehicles_Brands.objects.get(brand = query_vehicle_brand)
            return standardize_out(vehicle_brand)
        except:
            return standardize_out({"brand":[f'{query_vehicle_brand} not found']})
    
    def delete_a_brand(query_vehicle_brand):
        try:
            vehicle_brand = Vehicles_Brands.objects.get(brand = query_vehicle_brand)
        except:
            return json.dumps({'brand': ['brand not found to delete, please check the brand name']}) 
        else:
            vehicle_brand.delete()
        return standardize_out({"brand":[f'{query_vehicle_brand} deleted successfully']})