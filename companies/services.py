import json
from . import models
from django.forms.models import model_to_dict


class SCompanies():
    
    @staticmethod
    def save_company(company, address):
        
        new_address = models.Addresses(id=None, **address)
        new_address.save()
        
        new_company = models.Companies(**company, address = new_address)
        new_company.save()
        return json.dumps(model_to_dict( new_company))
    
