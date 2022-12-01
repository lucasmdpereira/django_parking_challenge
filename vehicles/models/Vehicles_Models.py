from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from . import Vehicles_Brands
from django.core.exceptions import ValidationError
from django.http import HttpResponse

from django.forms.models import model_to_dict
from vehicles.services import standardize_out, check_and_update_object

class Vehicles_Models(models.Model):
    model = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    brand = models.ForeignKey(Vehicles_Brands, on_delete = models.CASCADE)
    class Meta:
        db_table = 'vehicles_models';
        
    def post_a_vehicle_model(vehicle_model):
        try:
            vehicle_model['brand'] = Vehicles_Brands.objects.get(brand = vehicle_model['brand'])          
            new_vehicle_model = Vehicles_Models(**vehicle_model)
            try:
                new_vehicle_model.clean_fields()
                new_vehicle_model.save()
            except ValidationError as e:
                return HttpResponse(standardize_out(e.message_dict), status=422)
                
            return HttpResponse(standardize_out(new_vehicle_model), status=200)
        except:
            return HttpResponse(standardize_out({"models": ["Check model and brand names"]}), status=200)
        
    def put_a_vehicle_model(new_vehicle_model, query_vehicle_model):
        try:
            vehicle_model = Vehicles_Models.objects.get(model = query_vehicle_model)
            vehicle_model = check_and_update_object(model_to_dict(vehicle_model), new_vehicle_model)
        
            new_vehicle_model['brand'] = Vehicles_Brands.objects.get(brand = vehicle_model['brand'])           
            Vehicles_Models.objects.filter(pk = vehicle_model['id']).update(**new_vehicle_model)
            
            return HttpResponse(standardize_out(vehicle_model), status = 200)
        except:
            return HttpResponse(standardize_out({"model": ["Check model and brand names"]}), status=200)

    def get_a_vehicle_model(query_vehicle_model):
        try:
            vehicle_model = model_to_dict(Vehicles_Models.objects.get(model = query_vehicle_model))
            vehicle_model['brand'] = model_to_dict(Vehicles_Brands.objects.get(pk = vehicle_model['brand']))['brand']
            return HttpResponse(standardize_out(vehicle_model), status=200)
        except:
            return HttpResponse(standardize_out({"model": ["Check the model query"]}), status=200)
        
    def delete_a_vehicle_model(query_vehicle_model):
        try:
            vehicle_model = Vehicles_Models.objects.get(model = query_vehicle_model)
            vehicle_model.delete()
            return HttpResponse(standardize_out({"model":[f'{query_vehicle_model} deleted successfully']}), status=200)
        except:
            return HttpResponse(standardize_out({"model": ["Check the model query"]}), status=200)
        
