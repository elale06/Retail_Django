from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicios_list, name='listar_servicios'),
    path('crear/', views.servicio_crear),
    path('editar/<int:id>/', views.servicio_editar),
    path('eliminar/<int:id>/', views.servicio_eliminar),
    path('login/', views.login_servicios),
    path('precios/', views.precios),
]
