from django.http import HttpResponse
from parking.models import Parking_Control

import json

def vehicle_in(request):
    license_plate = json.loads(request.body)
    company_cnpj = license_plate.pop('company', None)
    license_plate = license_plate.pop('license_plate')
    return Parking_Control.vehicle_in(company_cnpj, license_plate)

def vehicle_out(request):
    company_and_license = json.loads(request.body)
    company_cnpj = company_and_license.pop('company', None)
    license_plate = company_and_license.pop('license_plate', None)
    return Parking_Control.vehicle_out(company_cnpj, license_plate)

    