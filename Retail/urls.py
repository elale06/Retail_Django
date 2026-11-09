from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth import views as auth_views
def menu(request):
    return render(request, 'menuApp/menu.html')

def informacion(request):
    return render(request, 'infoApp/info.html')

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
    path('informacion/', informacion),
    path('servicios/', include('serviciosApp.urls')),
    path('cuentas/login/', auth_views.loginView.as_view(
        template_name='serviciosApp/login_form.html'), name='login')
]
