# Generated by Django 4.1.3 on 2022-11-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_rename_company_id_addresses_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='phone',
            field=models.CharField(max_length=11),
        ),
    ]