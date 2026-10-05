from django.shortcuts import render, redirect, get_object_or_404
from .models import Servicio, PrecioServicio
from .forms import ServicioForm, PrecioServicioForm, PrecioServicioCrearForm

def login_servicios(request):
    return render(request, 'serviciosApp/login.html')

def servicios_list(request):
    servicios = Servicio.objects.all()
    return render(request, 'serviciosApp/listar.html', {'servicios': servicios})

def servicio_crear(request):
    form_servicio = ServicioForm(request.POST or None)
    form_precio = PrecioServicioCrearForm(request.POST or None)

    if request .method == 'POST':
        if form_servicio.is_valid() and form_precio.is_valid():
            servicio = form_servicio.save()
            precio = form_precio.save(commit=False)
            precio.servicio = servicio
            precio.save()
            return redirect('/servicios/')

    return render(request, 'serviciosApp/crear.html', {
        'form_servicio': form_servicio,
        'form_precio': form_precio
    })

def precio_crear(request):
    form = PrecioServicioCrearForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/servicios/')

    return render(request, 'serviciosApp/precio.html', {
        'form': form
    })
