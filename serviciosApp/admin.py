from django.contrib import admin
from .models import Servicio, PrecioServicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'disponibilidad')
    search_fields = ('nombre',)
    list_filter = ('disponibilidad',)
    ordering = ('id',)

@admin.register(PrecioServicio)
class PrecioServicioAdmin(admin.ModelAdmin):
    list_display = ('id', 'servicio', 'precio', 'moneda', 'descuento')
    search_fields = ('servicio__nombre',)
    list_filter = ('moneda',)
    ordering = ('id',)