from django.core.validators import validate_slug, MinLengthValidator, MaxLengthValidator
from django.db import models
from django.forms.models import model_to_dict
from django.http import HttpResponse

from vehicles.services import standardize_in, standardize_out, check_and_update_object
from . import Vehicles_Models


class Vehicles(models.Model):
    license_plate = models.CharField(max_length=7, unique=True, validators=[validate_slug])
    model = models.ForeignKey(Vehicles_Models, unique=False, on_delete = models.CASCADE)
    type_choices = [
        ('car', 'car'),
        ('bike', 'bike')
    ]
    type = models.CharField(max_length=20, choices=type_choices, default='car', unique=False, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    class Meta:
        db_table = 'vehicles';
    
    def post_a_vehicle(vehicle):
        try:
            vehicle['model'] = Vehicles_Models.objects.get(model = vehicle['model'])
        
            new_vehicle = Vehicles(**vehicle)
            new_vehicle.clean_fields()
            new_vehicle.save()
            return HttpResponse(standardize_out(new_vehicle), status=201)
        except:
            return HttpResponse(standardize_out({"error": ["Check model, type and license plate"]}), status=200)
        
    def put_a_vehicle(new_vehicle, query_vehicle):
        try:
            vehicle = Vehicles.objects.get(license_plate = query_vehicle)
            vehicle = check_and_update_object(model_to_dict(vehicle), new_vehicle)
            
            new_vehicle['model'] = Vehicles_Models.objects.get(model = new_vehicle['model'])
            
            Vehicles.objects.filter(pk = vehicle['id']).update(**new_vehicle)
            return HttpResponse(standardize_out(vehicle), status=200)
        except:
            return HttpResponse(standardize_out({"vehicle": ["Check model, type and license plate"]}), status=200)
    
    def get_a_vehicle(query_vehicle):
        try:
            vehicle = model_to_dict(Vehicles.objects.get(license_plate = query_vehicle))
            
            vehicle['model'] = model_to_dict(Vehicles_Models.objects.get(pk = vehicle['model']))    
            return HttpResponse(standardize_out(vehicle), status=200)
        except:
            return HttpResponse(standardize_out({"vehicle": ["Check the vehicle license plate"]}), status=200)
    
    def delete_a_vehicle(query_vehicle):
        try:
            vehicle = Vehicles.objects.get(license_plate = query_vehicle)
            vehicle.delete()
            return HttpResponse(standardize_out({"vehicle": [f'{query_vehicle} deleted successfully']}), status=200)
        except:
            return HttpResponse(standardize_out({"vehicle": ["Check the vehicle license plate"]}), status=200)
        
                             