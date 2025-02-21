from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('empresa/', views.empresa, name='empresa'),
    path('servicios/', views.servicios, name='servicios'),
    path('contacto/', views.contacto, name='contacto'),
]
