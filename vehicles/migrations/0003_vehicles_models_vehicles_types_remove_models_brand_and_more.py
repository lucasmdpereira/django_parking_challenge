# Generated by Django 4.1.3 on 2022-11-24 17:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0002_alter_vehicle_types_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicles_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(20)])),
            ],
            options={
                'db_table': 'vehicles_models',
            },
        ),
        migrations.CreateModel(
            name='Vehicles_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(20)])),
            ],
            options={
                'db_table': 'vehicles_type',
            },
        ),
        migrations.RemoveField(
            model_name='models',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='models',
            name='type',
        ),
        migrations.AlterField(
            model_name='brands',
            name='brand',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.MaxLengthValidator(20)]),
        ),
        migrations.DeleteModel(
            name='Vehicle_types',
        ),
        migrations.AddField(
            model_name='vehicles_models',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.brands'),
        ),
        migrations.AddField(
            model_name='vehicles_models',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicles_types'),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicles_models'),
        ),
        migrations.DeleteModel(
            name='Models',
        ),
    ]
