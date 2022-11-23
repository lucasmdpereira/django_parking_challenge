from django.forms.models import model_to_dict
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator,validate_slug
from django.core.exceptions import ValidationError

import vehicles
import json

class Brands(models.Model):
    brand = models.CharField(max_length=20, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    class Meta:
        db_table = 'brands';

class Vehicle_types(models.Model):
    type = models.CharField(max_length=20, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    class Meta:
        db_table = 'vehicle_types';

class Models(models.Model):
    model = models.CharField(max_length=20, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
    brand = models.ForeignKey(Brands, on_delete = models.CASCADE)
    type = models.ForeignKey(Vehicle_types, on_delete = models.CASCADE)
    class Meta:
        db_table = 'models';
        
class Vehicles(models.Model):
    license_plate = models.CharField(max_length=7, unique=True, validators=[validate_slug])
    model = models.ForeignKey(Models, on_delete = models.CASCADE)
    class Meta:
        db_table = 'vehicles';
                             