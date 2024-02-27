from django.urls import path
from Invoice_app.views import InvoiceView, InvoiceRetrieveView

urlpatterns =[
    path('invoice/', InvoiceView.as_view(), name= 'invoice'),
    path('invoice/<int:pk>/', InvoiceRetrieveView.as_view(), name= 'invoice-retrieve')
]