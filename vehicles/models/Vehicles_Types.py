# from django.core.validators import MinLengthValidator, MaxLengthValidator
# from django.db import models

# from vehicles.services import post_object, put_object, get_object, delete_object

# class Vehicles_Types(models.Model):
#     type = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
#     class Meta:
#         db_table = 'vehicles_types';
        
#     def post_a_vehicle_type(vehicle_type):
#         return post_object(vehicle_type, Vehicles_Types)
    
#     def put_a_vehicle_type(edited_vehicle_type, query_vehicle_type):
#         return put_object(edited_vehicle_type, query_vehicle_type, 'type', Vehicles_Types)

#     def get_a_vehicle_type(query_vehicle_type):
#         return get_object(query_vehicle_type, 'type', Vehicles_Types)
    
#     def delete_a_type(query_vehicle_type):
#         return delete_object(query_vehicle_type, 'type', Vehicles_Types)
        
