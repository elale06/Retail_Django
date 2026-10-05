from django.urls import path
from serviciosApp import views


urlpatterns = [
    path('', views.servicios, name='servicios'),
    path('precios/', views.precios, name='precios'),
]

