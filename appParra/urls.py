from django.urls import path
from appParra.view import *


urlpatterns = [

    path('inicio/', inicio),
    path('padre/', Padre),
    path('madre/', Madre),
    path('hija/', Hija),
    
    
]