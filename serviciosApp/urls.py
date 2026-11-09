from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicios_list, name='listar_servicios'),
    path('crear/', views.servicio_crear, name='crear_servicio'),
    path('editar/<int:id>/', views.editar_servicio, name='editar_servicio'),
    path('eliminar/<int:id>/', views.servicio_eliminar, name='eliminar_servicio'),

    path('login/', views.login_servicios, name='login_servicios'),
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('logout/', views.cerrar_servicios, name='cerrar_sesion'),

    #path('precios/', views.precio_crear, name='precios),
]
