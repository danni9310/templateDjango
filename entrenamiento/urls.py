# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import *

urlpatterns = [

    path(
        route='consulta',
        view= consulta,
        name='Consulta'
    ),

    path(
        route='respuesta',
        view= respuesta,
        name='Respuesta'
    ),
]