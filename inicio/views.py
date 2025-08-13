from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def crear_pelicula(request, pelicula, genero, pais):
    return(request, 'crear_pelicula.html')