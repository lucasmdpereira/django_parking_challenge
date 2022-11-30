from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from companies.models import Companies
from vehicles.models import Vehicles
from vehicles.services import standardize_out
from django.forms.models import model_to_dict

from django.utils.timezone import now


class Parking_Control(models.Model):
    entry_datetime = models.DateTimeField(auto_now_add=True)
    exit_datetime = models.DateTimeField(auto_now = False, default=None)
    company = models.ForeignKey(Companies, on_delete = models.CASCADE)
    vehicle = models.ForeignKey(Vehicles, on_delete = models.CASCADE)
    class Meta:
        db_table = 'parking_control';
    
    def vehicle_in(company_cnpj, vehicle_license_plate):
        company = Companies.objects.get(cnpj = company_cnpj)
        vehicle = Vehicles.objects.get(license_plate = vehicle_license_plate)
        
        parking_control_entry = Parking_Control.mount_object_to_save(company, vehicle)

        
        parking_control_entry = Parking_Control(**parking_control_entry)
        parking_control_entry.save()
        
        Parking_Control.check_spots(company, vehicle)
        
        return standardize_out(parking_control_entry)
    
    def vehicle_out(company_cnpj, vehicle_license_plate):
        vehicle = Vehicles.objects.get(license_plate = vehicle_license_plate)
        
        Parking_Control.objects.filter(vehicle = vehicle).filter(exit_datetime = None).update(exit_datetime = str(now()))
        
        return standardize_out({"msg": f'{model_to_dict(vehicle)["license_plate"]} is out'})       
    
    def mount_object_to_save(company, vehicle):
        parking_control_entry = {
            "company": company,
            "vehicle": vehicle
        }
        return parking_control_entry
    
    def check_spots(company, vehicle):
        vehicle_type = vehicle.model.type.type
        if vehicle_type == "car":
            pass
        if vehicle_type == "bike":
            teste = len(Parking_Control.objects.filter(company = company).filter(exit_datetime = None).filter(vehicle.model.type.type == 'bike'))
        
        
            return teste
        # teste = len(Parking_Control.objects.filter(company = company).filter(exit_datetime = None))

        

        