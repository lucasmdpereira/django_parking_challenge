from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
import json

@staticmethod
def check_and_update_object(object, edited_object ):
    for key in object:
        if (key in edited_object):
            object[key] = edited_object[key]           
    return object


# @staticmethod
# def standardize_in(object):
#     for key in object.keys():
#         object[key] = str(object[key]).strip().lower()
#     return object

# @staticmethod
# def standardize_out(object):
#     if (type(object) is dict):
#         standardized_object = object
#     else:
#         try:
#             standardized_object = model_to_dict(object) 
#         except:
#             return json.dumps({"Error": "Invalid object"})
#     return json.dumps(standardized_object)

# @staticmethod
# def check_and_update_object(object, edited_object ):
#     for key in object:
#         if (key in edited_object):
#             object[key] = edited_object[key]           
#     return object

# @staticmethod
# def post_object(object, object_model):
#     object = standardize_in(object)
#     new_object = object_model(**object)
#     try:
#         new_object.clean_fields()
#         try:
#             new_object.save()
#             return standardize_out(new_object)
#         except:
#             return standardize_out({"error": f'{list(object.values())[0]} already exists'})
#     except ValidationError as e:
#         return standardize_out(e.message_dict)
    
# @staticmethod
# def put_object(edited_object, object_query, object_key, object_model):
#     try:
#         object = find_object_by_key(object_query, object_key, object_model)
#         object = check_and_update_object(object, edited_object)
#         object_model.objects.filter(pk = object['id']).update(**edited_object)
#         return standardize_out(object)              
#     except ValidationError as e:
#         return standardize_out(e.message_dict)

# @staticmethod
# def get_object(object_query, object_key, object_model):
#     try:
#         object = find_object_by_key(object_query, object_key, object_model)
#         return standardize_out(object)
#     except:
#         return standardize_out({"error":[f'{object_query} not found']})
    
# @staticmethod
# def delete_object(object_query, object_key, object_model):
#     object = find_object_by_key(object_query, object_key, object_model) 
#     object.delete()
#     return standardize_out({"msg":[f'{object_query} deleted successfully']})

# @staticmethod
# def find_object_by_key(object_query, object_key, object_model):
#     if (object_key == 'brand'): 
#         return object_model.objects.filter(brand__contains = object_query).get()
#     if (object_key == 'type'):
#         return object_model.objects.filter(type__contains = object_query).get()
