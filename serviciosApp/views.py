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
    form = PrecioServicioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/servicios/')

    return render(request, 'serviciosApp/precio.html', {
        'form': form
    })

def editar_servicio(request, id):
    servicio = get_object_or_404(Servicio, id = id)

    precio, created = PrecioServicio.objects.get_or_create(
        servicio = servicio,
        defaults = {
            'precio': 0,
            'descuento': 0,
            'moneda': 'CLP',
            'observacion': ''
        }
    )

    if request.method == 'POST':
        servicio.nombre = request.POST.get('nombre') or servicio.nombre
        servicio.descripcion = request.POST.get('descripcion') or servicio.descripcion
        servicio.disponibilidad = request.POST.get('disponibilidad') or servicio.disponibilidad
        servicio.save()

        precio.precio = request.POST.get('precio') or precio.precio
        precio.descuento = request.POST.get('descuento') or precio.descuento
        precio.moneda = request.POST.get('moneda') or precio.moneda
        precio.observacion = request.POST.get('observacion') or precio.observacion
        precio.save()

        return redirect('listar_servicios')

    return render(request, 'serviciosApp/editar.html', {
        'servicio': servicio,
        'precio': precio
    })

def servicio_eliminar(request, id):
    servicio = get_object_or_404(Servicio, id=id)
    servicio.delete()
    return redirect('listar_servicios')