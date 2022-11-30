from django.core.validators import validate_slug, MinLengthValidator, MaxLengthValidator
from django.db import models
from django.forms.models import model_to_dict

from vehicles.services import standardize_in, standardize_out, check_and_update_object
from . import Vehicles_Models


class Vehicles(models.Model):
    license_plate = models.CharField(max_length=7, unique=True, validators=[validate_slug])
    model = models.ForeignKey(Vehicles_Models, on_delete = models.CASCADE)
    type = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    class Meta:
        db_table = 'vehicles';
    
    def post_a_vehicle(vehicle):
        try:
            vehicle['model'] = Vehicles_Models.objects.get(model = vehicle['model'])
        
            new_vehicle = Vehicles(**vehicle)
            new_vehicle.save()
            return standardize_out(new_vehicle)
        except:
            return standardize_out({"error": ["Check model,and license plate"]})
        
    def put_a_vehicle(new_vehicle, query_vehicle):
        try:
            vehicle = Vehicles.objects.get(license_plate = query_vehicle)
            vehicle = check_and_update_object(model_to_dict(vehicle), new_vehicle)
            
            new_vehicle['model'] = Vehicles_Models.objects.get(model = new_vehicle['model'])
            
            Vehicles.objects.filter(pk = vehicle['id']).update(**new_vehicle)
            return standardize_out(vehicle)
        except:
            return standardize_out({"error": ["Check model,and license plate"]})
    
    def get_a_vehicle(query_vehicle):
        try:
            vehicle = model_to_dict(Vehicles.objects.get(license_plate = query_vehicle))
            
            vehicle['model'] = model_to_dict(Vehicles_Models.objects.get(pk = vehicle['model']))    
            return standardize_out(vehicle)
        except:
            return standardize_out({"error": ["Check the vehicle license plate"]})
    
    def delete_a_vehicle(query_vehicle):
        try:
            vehicle = Vehicles.objects.get(license_plate = query_vehicle)
            vehicle.delete()
            return standardize_out({"msg": [f'{query_vehicle} deleted successfully']})
        except:
            return standardize_out({"error": ["Check the vehicle license plate"]})
        
                             