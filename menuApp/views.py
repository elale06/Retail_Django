from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def menu(request):
    return render(request, 'menuApp/menu.html')

"""
def menu(request):
    titulo = "<h1>Menú</h1>"
    logo = "<img src='https://cdn.hashnode.com/res/hashnode/image/upload/v1636780048014/niLN2J80j.png' width=200 heigth=100 />"
    links = '''
    <ul>
        <li><a href="informacion">Información</a></li>
        <li><a href="servicios">Servicios</a></li>
        <li><a href="servicios/precios">Precios</a></li>
    </ul>
    '''
    pagina = titulo + logo + links
    return HttpResponse(pagina)
"""