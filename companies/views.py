from django.http import HttpResponse
from .models import Companies
import json

def index(request):
    return HttpResponse("Hello, world. You're at the companies index.")

def post(request):
    company = json.loads(request.body)
    address = company.pop("address", None)
    return Companies.post_a_company(company, address)

def put(request, cnpj):
    company = json.loads(request.body)
    address = company.pop("address", None)
    return HttpResponse(Companies.put_a_company(company, address, cnpj))

def get(request, cnpj):
    return HttpResponse(Companies.get_a_company(cnpj))

def delete(request, cnpj):
    return HttpResponse(Companies.delete_a_company(cnpj))