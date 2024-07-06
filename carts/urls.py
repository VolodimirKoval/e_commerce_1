from django.urls import path
from .views import cart_add, cart_change, cart_remove


app_name = 'carts'

urlpatterns = [
    path('cart_add/<slug:product_slug>', cart_add, name='cart_add'),
    path('cart_change/<slug:product_slug>', cart_change, name='cart_change'),
    path('cart_remove/<int:cart_id>', cart_remove, name='cart_remove'),
]