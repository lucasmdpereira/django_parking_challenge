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
        address = Addresses.objects.filter(id = query_id).get()
        
        return address

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
        
        return Companies.standardize_a_company(new_company, new_address)
    
    def put_a_company(edited_company, edited_address, query_cnpj):
        company = model_to_dict(Companies.find_a_company_in_db(query_cnpj))
        address = model_to_dict(Addresses.find_a_address_in_db(company['address']))       
        
        for key in company:
            if (key in edited_company):
                company[key] = edited_company[key]    
                
        for key in address:
            if (key in edited_address):
                address[key] = edited_address[key]  
        
        Companies.objects.filter(pk = company['id']).update(**company)
        Addresses.objects.filter(pk = address['id']).update(**address)

        return Companies.standardize_a_company(company, address)
        
    def get_a_company(query_cnpj):       
        return json.dumps(model_to_dict(Companies.find_a_company(query_cnpj)))
        
    def delete_a_company(query_cnpj):
        company = Companies.find_a_company(query_cnpj)
        company.delete()
        
        return json.dumps('Company deleted successfully')
    
    @staticmethod
    def find_a_company_in_db(query_cnpj):
        company = Companies.objects.filter(cnpj = query_cnpj).get()
        return company
    
    @staticmethod
    def standardize_a_company(company, address):
        if (type(company) is dict):
            standardized_company = company
            standardized_company['address'] = address
        elif(type(company) is companies.models.Companies):
            standardized_company = model_to_dict(company)
            standardized_company['address'] = model_to_dict(address)
        return json.dumps(standardized_company)
        
    

    
