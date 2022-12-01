from django.test import TestCase
from django.test import Client
from companies.models import Companies, Addresses

import json

company = {
    "name": "name",
    "cnpj": "1",
    "phone": "5500900000000",
    "address":{
        "cep": 1111111,
        "street": "street",
        "number": 1,
        "others": "others"
    },
    "bike_parking_spots": 10,
    "car_parking_spots": 5
}

class Test_Companies(TestCase):
    def setUp(self):
        self.c = Client()
        
    def test_POST_company_with_all_valid_fields(self):
        """
        The post_a_company function must receive 2 objects (company, address) and add them to the database
        """
       
        response = self.c.post('/companies/post', json.dumps(company), content_type="application/json")
        
        if (response.status_code == 201):
            print("✅ test_create_a_company_with_all_valid_fields")
        else:
            print("❌ test_create_a_company_with_all_valid_fields")
        
        self.assertEqual(response.status_code, 201)
        
    def test_create_a_company_without_required_fields(self):
        """
        The post_a_company function should return error 422 on missing any field except "others"
        """
        
        for key in company:
            self.company = company
            if key != 'address':
                self.company[key] = ""        
                response = self.c.post('/companies/post', json.dumps(self.company), content_type="application/json")
                
                if (response.status_code == 422):
                    print(f"✅ test_create_a_company_without_required_fields - field: {key}")
                else:
                    print(f"❌ test_create_a_company_without_required_fields")
                
                self.assertEqual(response.status_code, 422)
        