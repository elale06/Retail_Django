from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from .models import Servicio, PrecioServicio
from .forms import ServicioForm, PrecioServicioForm, PrecioServicioCrearForm

def login_servicios(request):
    if request.user.is_authenticated:
        return redirect('listar_servicios')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('listar_servicios')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    # Mostrar el formulario real de inicio de sesión
    return render(request, 'serviciosApp/login_form.html')

def registro_usuario(request):
    if request.user.is_authenticated:
        return redirect('listar_servicios')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not username or not password or not password2:
            messages.error(request, 'Todos los campos son obligatorios.')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Este usuario ya existe.')
        elif password != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
        else:
            # Validar contraseña según settings.py
            try:
                validate_password(password)

                # Crear usuario utilizando el sistema seguro de Django
                User.objects.create_user(
                    username=username,
                    password=password
                )

                messages.success(
                    request,
                    'Registrado exitosamente. Ahora puedes iniciar sesión.'
                )

                return redirect('login_servicios')
            except ValidationError as error:
                for mensaje in error.messages:
                    messages.error(request, mensaje)
    return render(request, 'serviciosApp/registro.html')

@login_required(login_url='login_servicios')
def cerrar_sesion(request):
    if request.method == 'POST':
        login(request)
        return redirect('login_servicios')
    return redirect('listar_servicios')

@login_required(login_url='login_servicios')
def servicios_list(request):
    servicios = Servicio.objects.all()
    return render(request, 'serviciosApp/listar.html', {'servicios': servicios})

@login_required(login_url='login_servicios')
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

@login_required(login_url='login_servicios')
def precio_crear(request):
    form = PrecioServicioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/servicios/')

    return render(request, 'serviciosApp/precio.html', {
        'form': form
    })

@login_required(login_url='login_servicios')
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

@login_required(login_url='login_servicios')
def servicio_eliminar(request, id):
    servicio = get_object_or_404(Servicio, id=id)

    if request.method == 'POST':
        servicio.delete()
        return redirect('listar_servicios')

    return render(request, 'serviciosApp/eliminar.html', {
        'servicio': servicio
    })