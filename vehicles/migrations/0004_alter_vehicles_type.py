# Generated by Django 4.1.3 on 2022-11-30 13:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_alter_vehicles_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='type',
            field=models.CharField(choices=[('car', 'car'), ('bike', 'bike')], default='car', max_length=20, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(20)]),
        ),
    ]
