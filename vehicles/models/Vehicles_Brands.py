from django.forms.models import model_to_dict
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.db import models

from setup.services import standardize_in, standardize_out, check_and_update_object

class Vehicles_Brands(models.Model):
    brand = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    class Meta:
        db_table = 'vehicles_brands';
           
    # TODO :recycle: user services.check_and_save_object       
    def post_a_brand(vehicle_brand):
        vehicle_brand = standardize_in(vehicle_brand)
        new_vehicle_brand = Vehicles_Brands(**vehicle_brand)
        try:
            new_vehicle_brand.clean_fields() 
            try:
                new_vehicle_brand.save()
                return standardize_out(new_vehicle_brand)
            except:
               return standardize_out({"brand":["The vehicle brand already exists"]}) 
        except ValidationError as e:
            return standardize_out(e.message_dict)
        
    def put_a_brand(edited_vehicle_brand, query_vehicle_brand):
        try:
            vehicle_brand = model_to_dict(Vehicles_Brands.objects.filter(brand=query_vehicle_brand).get()) 
            vehicle_brand = check_and_update_object(vehicle_brand, edited_vehicle_brand)
            Vehicles_Brands.objects.filter(pk = vehicle_brand['id']).update(**edited_vehicle_brand)
            return standardize_out(vehicle_brand)              
        except ValidationError as e:
            return standardize_out(e.message_dict)
    
    # TODO :sparkles: usar mesmo sistema em companies.models.get_a_company
    def get_a_brand(query_vehicle_brand):
        try:
            vehicle_brand = Vehicles_Brands.objects.filter(brand = query_vehicle_brand).get()
            return standardize_out(vehicle_brand)
        except:
            return standardize_out({"brand":[f'Brand {query_vehicle_brand} not found']})
    
    def delete_a_brand(query_vehicle_brand):
        vehicle_brand = Vehicles_Brands.objects.filter(brand = query_vehicle_brand).get()
        vehicle_brand.delete()
        return standardize_out({"brand":["Brand deleted successfully"]})