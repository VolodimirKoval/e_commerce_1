from django.urls import path
from .views import products, product


app_name = 'shop'

urlpatterns = [
    path('search/', products, name='search'),
    path('products/<slug:category_slug>/', products, name='products'),
    path('product/<slug:product_slug>/', product, name='product'),
]
