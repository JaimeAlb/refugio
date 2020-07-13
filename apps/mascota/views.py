from django.shortcuts import render
from django.http import HttpResponse
from .models import Mascota


def index(request):
    return render(request, 'index.html')

"""
def mascotas_list(request):
    mascota = Mascota.objects.all()
    contexto = {'mascotas_lista':mascota}
    return render(request, 'mascotas_list.html', contexto)
    
"""