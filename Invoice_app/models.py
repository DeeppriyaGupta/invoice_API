from django.db import models

class Invoice(models.Model):
    date = models.DateField()
    customer_name = models.CharField(max_length = 100)

class Invoice_Detial(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete = models.CASCADE)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
