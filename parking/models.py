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
        try:
            company = Companies.objects.get(cnpj = company_cnpj)
            vehicle = Vehicles.objects.get(license_plate = vehicle_license_plate)
            
            parking_control_entry = Parking_Control.mount_object_to_save(company, vehicle)

            
            parking_control_entry = Parking_Control(**parking_control_entry)
            
            left_spots = Parking_Control.check_left_spots(company, vehicle)
            if left_spots > 1:
                parking_control_entry.save()
                return standardize_out({"parking_in":[f"Vehicle {vehicle_license_plate} enter at {str(now())}", f"There's {left_spots} more spot for {vehicle.type}"]})
            elif left_spots == 1:
                parking_control_entry.save()
                return standardize_out({"parking_in":[f"Vehicle {vehicle_license_plate} enter at {str(now())}", f"WARNING, there's one more spot for {vehicle.type}"]})
            elif left_spots <= 0:
                return standardize_out({"parking_in":[f"Sorry, we are full"]})
            

        except:
            standardize_out({"parking_in": ["Check de vehicle license plate and company"]})

    def vehicle_out(company_cnpj, vehicle_license_plate):
        try:
            vehicle = Vehicles.objects.get(license_plate = vehicle_license_plate)
            
            Parking_Control.objects.filter(vehicle = vehicle).filter(exit_datetime = None).update(exit_datetime = str(now()))
            
            return standardize_out({"msg": f'{model_to_dict(vehicle)["license_plate"]} is out'})   
        except:
            standardize_out({"parking_out": ["Check de vehicle license plate and company"]})    
    
    def mount_object_to_save(company, vehicle):
        parking_control_entry = {
            "company": company,
            "vehicle": vehicle
        }
        return parking_control_entry
    
    def check_left_spots(company, vehicle):
        vehicle_type = vehicle.type
        vehicles_in_parking = list(Parking_Control.objects.filter(company = company).filter(exit_datetime = None))
         
        vehicles_of_the_type_parking = 0
        for vehicle in vehicles_in_parking:
            if (vehicle.vehicle.type == vehicle_type):
                vehicles_of_the_type_parking += 1
                
        if vehicle_type == 'car':
            left_spots = company.car_parking_spots - vehicles_of_the_type_parking
        elif vehicle_type == 'bike':
            left_spots = company.bike_parking_spots - vehicles_of_the_type_parking
            
        return left_spots


        

        