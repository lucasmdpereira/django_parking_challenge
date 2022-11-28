from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.db import models

from setup.services import check_and_update_object, post_object, standardize_out, put_object

class Vehicles_Types(models.Model):
    type = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    class Meta:
        db_table = 'vehicles_types';
        
    def post_a_vehicle_type(vehicle_type):
        return post_object(vehicle_type, Vehicles_Types)
    
    def put_a_vehicle_type(edited_vehicle_type, query_vehicle_type):
        return put_object(edited_vehicle_type, query_vehicle_type, 'type' ,Vehicles_Types)
        # try:
        #     vehicle_type = Vehicles_Types.objects.filter(type=query_vehicle_type) 
        #     vehicle_type = check_and_update_object(vehicle_type, edited_vehicle_type)
        #     Vehicles_Types.objects.filter(pk = vehicle_type['id']).update(**edited_vehicle_type)
        #     return standardize_out(vehicle_type)              
        # except ValidationError as e:
        #     return standardize_out(e.message_dict)
        
