# from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_slug
# from django.core.exceptions import ValidationError
# from django.db import models

# from setup.services import standardize_in, standardize_out, check_and_update_object

# class Vehicles_models(models.Model):
#     model = models.CharField(max_length=20, validators=[MinLengthValidator(3), MaxLengthValidator(20)])
#     brand = models.ForeignKey(Vehicles_Brands, on_delete = models.CASCADE)
#     type = models.ForeignKey(Vehicles_Types, on_delete = models.CASCADE)
#     class Meta:
#         db_table = 'vehicles_models';
        
#     def post_a_Vehicles_models(vehicles_models):
#         new_vehicle_type = Vehicles_models(**vehicles_models)
#         new_vehicle_type.save()
        
# class Vehicles(models.Model):
#     license_plate = models.CharField(max_length=7, unique=True, validators=[validate_slug])
#     model = models.ForeignKey(Vehicles_models, on_delete = models.CASCADE)
#     class Meta:
#         db_table = 'vehicles';
        
                             