from rest_framework import serializers
from Invoice_app.models import Invoice, Invoice_Detial

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class Invoice_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice_Detial
        fields = '__all__'       