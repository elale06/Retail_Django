from django.shortcuts import render

def inicio(request):
    return render(request, 'infoApp/index.html')