from django.urls import path
from .views import *
from Restaurent.views import * 




urlpatterns = [
    path('', index, name="index"),
    
]
