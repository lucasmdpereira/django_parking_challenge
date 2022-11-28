# Generated by Django 4.1.3 on 2022-11-24 17:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_vehicles_models_vehicles_types_remove_models_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='brand',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(20), django.core.validators.ProhibitNullCharactersValidator('')]),
        ),
    ]
