from .views import index, about, delivery_and_payment, contacts
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('delivery_and_payment/', delivery_and_payment, name='delivery_and_payment'),
    path('contacts/', contacts, name='contacts'),
]
