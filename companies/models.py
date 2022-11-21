from django.db import models

class Companies(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14)
    phone = models.CharField(max_length=11)
    bike_parking_spots = models.IntegerField(default=0)
    car_parking_spots = models.IntegerField(default=0)
    
class Addresses(models.Model):
    company_id = models.ForeignKey(Companies, on_delete=models.CASCADE)
    cep = models.CharField(max_length=8)
    street = models.CharField(max_length=255)
    number = models.IntegerField(max_length=255)
    others = models.CharField(max_length=255)