"""
urls de todas las vistas que van a manejar el enrutador a todas 
los endpoints disponibles para la api
"""

from django.urls import path
from api import views


urlpatterns = [
    path('get_all', views.get_all, name='get_all'),
    path('filter&name=<str:name>', views.filter, name='filter'),
]
