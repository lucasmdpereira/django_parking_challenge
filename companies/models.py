from django.db import models
from . import services

import json

class Addresses(models.Model):
    cep = models.CharField(max_length=8)
    street = models.CharField(max_length=255)
    number = models.PositiveSmallIntegerField()
    others = models.CharField(max_length=255)
    class Meta:
        db_table = 'addresses';

class Companies(models.Model):
    name = models.CharField(max_length=50, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)
    phone = models.CharField(max_length=11, unique=True)
    address = models.OneToOneField(Addresses, on_delete = models.CASCADE)
    bike_parking_spots = models.PositiveSmallIntegerField(default=0) # 0 a 32767
    car_parking_spots = models.PositiveSmallIntegerField(default=0)
    class Meta:
        db_table = 'companies';
    
    def post_a_company(company, address):
        return services.SCompanies.save_company(company, address)
    
    def get_a_company(cnpj):
        company = Companies.objects.filter(cnpj = cnpj)
        return company
        
    
