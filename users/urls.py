from django.urls import path
from .views import login, logout, profile, registration, user_cart

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('registration/', registration, name='registration'),
    path('user-cart/', user_cart, name='user-cart'),
]
