from django.db import models
from django.forms.models import model_to_dict
from django.http import HttpResponse

from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError

from companies.services import standardize_a_company
from setup.services import check_and_update_object

import json

class Addresses(models.Model):
    cep = models.PositiveIntegerField(validators=[MinValueValidator(1000000), MaxValueValidator(99999999)]) # https://suporte.boxloja.pro/article/90-faixa-de-ceps-do-brasil
    street = models.CharField(max_length=255, validators=[MinLengthValidator(3), MaxLengthValidator(255)])
    number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(32767)])
    others = models.CharField(max_length=255, blank=True, null=True, validators=[MaxLengthValidator(255)])
    class Meta:
        db_table = 'addresses';
        
    @staticmethod
    def find_a_address_in_db(query_id):
        return Addresses.objects.filter(id = query_id).get()
    
    # TODO :recycle: Criar método save_a_address_in_db, está estranho a classe Companies fazer isso

class Companies(models.Model):
    name = models.CharField(max_length=50, unique=True, validators=[MaxLengthValidator(50)])
    cnpj = models.PositiveIntegerField(unique=True, validators=[MaxValueValidator(99999999999999)])
    phone = models.IntegerField(unique=True, validators=[MinValueValidator(5500900000000), MaxValueValidator(5599999999999)]) # Only Brazilian numbers are valid
    address = models.OneToOneField(Addresses, on_delete = models.CASCADE)
    bike_parking_spots = models.PositiveSmallIntegerField(default=0) # 0 a 32767
    car_parking_spots = models.PositiveSmallIntegerField(default=0)
    class Meta:
        db_table = 'companies';
    
    def post_a_company(company, address):
        try:
            new_address = Addresses(**address)
            
            try:
                new_address.clean_fields()
                new_address.save()
            except ValidationError as e:
                return HttpResponse(json.dumps(e.message_dict), status=422)
        
            new_company = Companies(**company, address=new_address)
            
            try:
                new_company.clean_fields()
                new_company.save()
            except ValidationError as e:
                return HttpResponse(json.dumps(e.message_dict), status=422)
        
            return HttpResponse(standardize_a_company(new_company, Companies, Addresses), status=201)
            
        except:
            return HttpResponse(json.dumps({"company": ["The company name, cnpj and phone must be unique"]}), status=409)
    
    def put_a_company(edited_company, edited_address, query_cnpj):
        company = model_to_dict(Companies.find_a_company_in_db(query_cnpj))
        address = model_to_dict(Addresses.find_a_address_in_db(company['address']))       
        
        company = check_and_update_object(company, edited_company)
        address = check_and_update_object(address, edited_address)
               
        Companies.objects.filter(pk = company['id']).update(**company)
        Addresses.objects.filter(pk = address['id']).update(**address)

        return standardize_a_company(company, Companies, Addresses)
        
    # TODO :sparkles: criar retorno caso não encontre nenhuma empresa
    def get_a_company(query_cnpj):       
        company = Companies.find_a_company_in_db(query_cnpj)
        return standardize_a_company(company, Companies, Addresses)
        
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

    
