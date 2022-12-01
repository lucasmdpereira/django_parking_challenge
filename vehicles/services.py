from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
import json

@staticmethod
def standardize_in(object):
    for key in object.keys():
        object[key] = str(object[key]).strip().lower()
    return object

@staticmethod
def standardize_out(object):
    if (type(object) is dict):
        standardized_object = object
    else:
        try:
            standardized_object = model_to_dict(object) 
        except:
            return json.dumps({"Error": "Invalid object"})
    return json.dumps(standardized_object)

@staticmethod
def check_and_update_object(object, edited_object ):
    for key in object:
        if (key in edited_object):
            object[key] = edited_object[key]           
    return object

