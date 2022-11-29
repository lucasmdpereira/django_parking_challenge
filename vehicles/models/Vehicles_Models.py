from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from . import Vehicles_Brands, Vehicles_Types

from django.forms.models import model_to_dict
from vehicles.services import standardize_out, check_and_update_object

class Vehicles_Models(models.Model):
    model = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    brand = models.ForeignKey(Vehicles_Brands, on_delete = models.CASCADE)
    type = models.ForeignKey(Vehicles_Types, on_delete = models.CASCADE)
    class Meta:
        db_table = 'vehicles_models';
        
    def post_a_vehicle_model(vehicle_model):
        try:
            vehicle_model['brand'] = Vehicles_Brands.objects.get(brand = vehicle_model['brand'])
            vehicle_model['type'] =  Vehicles_Types.objects.get(type = vehicle_model['type'])
            
            new_vehicle_model = Vehicles_Models(**vehicle_model)
            new_vehicle_model.save()
            
            return standardize_out(new_vehicle_model)
        except:
            return standardize_out({"error": ["Check model, brand and type names"]})
        
    def put_a_vehicle_model(new_vehicle_model, query_vehicle_model):
        try:
            vehicle_model = Vehicles_Models.objects.get(model = query_vehicle_model)
            vehicle_model = check_and_update_object(model_to_dict(vehicle_model), new_vehicle_model)
        
            new_vehicle_model['brand'] = Vehicles_Brands.objects.get(brand = vehicle_model['brand'])
            new_vehicle_model['type'] =  Vehicles_Types.objects.get(type = vehicle_model['type'])
            
            Vehicles_Models.objects.filter(pk = vehicle_model['id']).update(**new_vehicle_model)
            
            return standardize_out(vehicle_model)
        except:
            return standardize_out({"error": ["Check model, brand and type names"]})

    def get_a_vehicle_model(query_vehicle_model):
        try:
            vehicle_model = model_to_dict(Vehicles_Models.objects.get(model = query_vehicle_model))
            vehicle_model['brand'] = model_to_dict(Vehicles_Brands.objects.get(pk = vehicle_model['brand']))['brand']
            vehicle_model['type'] =  model_to_dict(Vehicles_Types.objects.get(pk = vehicle_model['type']))['type']

            return standardize_out(vehicle_model)
        except:
            return standardize_out({"error": ["Check model, brand and type names"]})
        
    def delete_a_vehicle_model(query_vehicle_model):
        try:
            vehicle_model = Vehicles_Models.objects.get(model = query_vehicle_model)
            vehicle_model.delete()
            return standardize_out({"msg":[f'{query_vehicle_model} deleted successfully']})
        except:
            return standardize_out({"error": ["Check model, brand and type names"]})
        
