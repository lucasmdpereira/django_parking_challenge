from django.forms.models import model_to_dict
from django.db import models

import companies
import json

class Addresses(models.Model):
    cep = models.CharField(max_length=8)
    street = models.CharField(max_length=255)
    number = models.PositiveSmallIntegerField()
    others = models.CharField(max_length=255)
    class Meta:
        db_table = 'addresses';
        
    @staticmethod
    def find_a_address_in_db(query_id):
        return Addresses.objects.filter(id = query_id).get()

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
        new_address = Addresses(id=None, **address)
        new_address.save()
        
        new_company = Companies(**company, address=new_address)
        new_company.save()
        
        return Companies.standardize_a_company(new_company)
    
    def put_a_company(edited_company, edited_address, query_cnpj):
        company = model_to_dict(Companies.find_a_company_in_db(query_cnpj))
        address = model_to_dict(Addresses.find_a_address_in_db(company['address']))       
        
        company = Companies.check_and_update_object(company, edited_company)
        address = Companies.check_and_update_object(address, edited_address)
               
        Companies.objects.filter(pk = company['id']).update(**company)
        Addresses.objects.filter(pk = address['id']).update(**address)

        return Companies.standardize_a_company(company)
        
    def get_a_company(query_cnpj):       
        company = Companies.find_a_company_in_db(query_cnpj)
        return Companies.standardize_a_company(company)
        
    def delete_a_company(query_cnpj):
        company = Companies.find_a_company_in_db(query_cnpj)
        company.delete()
        
        return json.dumps('Company deleted successfully')
    
    @staticmethod
    def find_a_company_in_db(query_cnpj):
        try:
            company = Companies.objects.filter(cnpj = query_cnpj).get()
        except:
            company = []
        return company
    
    @staticmethod
    def standardize_a_company(company):
        if (type(company) is dict):
            standardized_company = company
        elif(type(company) is companies.models.Companies):
            standardized_company = model_to_dict(company)
        else:
            return {}           
    
        address = Addresses.find_a_address_in_db(standardized_company['address']) 
        standardized_company['address'] = model_to_dict(address)  
        # standardized_company.pop('id', None) # remove the id from the company object
        # standardized_company['address'].pop('id', None) # remove the id from the address object
        return json.dumps(standardized_company)
    
    @staticmethod
    def check_and_update_object(object, edited_object ):
        for key in object:
            if (key in edited_object):
                object[key] = edited_object[key]           
        return object

    
