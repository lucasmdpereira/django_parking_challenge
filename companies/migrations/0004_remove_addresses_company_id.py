# Generated by Django 4.1.3 on 2022-11-22 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_remove_companies_company_id_companies_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addresses',
            name='company_id',
        ),
    ]