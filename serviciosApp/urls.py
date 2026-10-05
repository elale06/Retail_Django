from django.urls import path
from serviciosApp import views

urlpatterns = [
    path('', views.servicios, name='servicios'),
    path('crear/', views.servicio_crear),
    path('editar/<int:id>/', views.servicio_editar),
    path('eliminar/<int:id>/', views.servicio_eliminar),
    path('login/', views.login_servicios),
    path('precios/', views.precios),
]
