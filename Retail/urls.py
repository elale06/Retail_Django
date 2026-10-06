from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def menu(request):
    return render(request, 'menuApp/menu.html')

def informacion(request):
    return render(request, 'infoApp/info.html')

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
    path('informacion/', informacion),
    path('servicios/', include('serviciosApp.urls')),
]
