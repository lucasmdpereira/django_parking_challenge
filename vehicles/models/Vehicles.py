# from django.core.validators import MinLengthValidator, MaxLengthValidator, validate_slug
# from django.core.exceptions import ValidationError
# from django.db import models

# from setup.services import standardize_in, standardize_out, check_and_update_object

# class Vehicles(models.Model):
#     license_plate = models.CharField(max_length=7, unique=True, validators=[validate_slug])
#     model = models.ForeignKey(Vehicles_models, on_delete = models.CASCADE)
#     class Meta:
#         db_table = 'vehicles';
        
                             