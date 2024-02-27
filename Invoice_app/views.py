from django.shortcuts import render
from Invoice_app.models import Invoice, Invoice_Detial
from Invoice_app.serializers import InvoiceSerializer, Invoice_DetailSerializer
from rest_framework import generics

class InvoiceView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
