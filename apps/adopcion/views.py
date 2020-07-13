from django.shortcuts import render
from django.http import HttpResponse


def index_adopcion(request):
    return HttpResponse("Pagina principal app adopcion")
    
