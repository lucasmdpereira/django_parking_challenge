from django.forms.models import model_to_dict
import json

@staticmethod
def standardize_a_company(company, Companies, Addresses):
    if (type(company) is dict):
        standardized_company = company
    elif(type(company) is Companies): 
        standardized_company = model_to_dict(company)
    else:
        return {}           

    address = Addresses.find_a_address_in_db(standardized_company['address']) 
    standardized_company['address'] = model_to_dict(address)  
    
    # standardized_company.pop('id', None) # remove the id from the company object
    # standardized_company['address'].pop('id', None) # remove the id from the address object
    
    return json.dumps(standardized_company)