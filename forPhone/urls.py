from django.urls import path
from .views import *


urlpatterns = [
    path('', homePage, name='homePage'),
    path('login/', userAuth, name='login'),
    path('createshop/', createShop, name='createShop'),
]


