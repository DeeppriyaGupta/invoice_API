from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from Invoice_app.models import Invoice, Invoice_Detial

class InvoiceTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create(self):
        data= {'date': '2024-02-11', 'customer_name': 'deeppriya gupta'}
        response = self.client.post('/invoice/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_retrieve(self):
        i= Invoice.objects.create(date= '2024-02-11', customer_name= 'deeppriya gupta')
        print(i.id)
        response = self.client.get(f'/invoice/{i.id}/')
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
