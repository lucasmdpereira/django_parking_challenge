from django.http import HttpResponse
from .models import Companies
import json

def index(request):
    return HttpResponse("Hello, world. You're at the companies index.")

def post(request):
    company = json.loads(request.body)
    address = company.pop("address", None)
    return HttpResponse(Companies.post_a_company(company, address))

# def get(request):
#     cnpj = request.headers['id']
#     return HttpResponse('ok')
#     # cnpj = json.loads(request.body)
#     # return HttpResponse(Companies.get_a_company(cnpj))