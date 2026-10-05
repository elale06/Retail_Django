from django import forms
from .models import Servicio, PrecioServicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class PrecioServicioCrearForm(forms.ModelForm):
    class Meta:
        model = PrecioServicio
        fields = ['precio', 'descuento', 'moneda', 'observacion']

class PrecioServicioForm(forms.ModelForm):
    class Meta:
        model = PrecioServicio
        fields = '__all__'
