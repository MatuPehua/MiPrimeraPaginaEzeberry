from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Peliculas

def inicio(request):
    return render(request, 'inicio.html')

def crear_pelicula(request, pelicula, genero, pais):
    pelicula = Peliculas(pelicula=pelicula, genero=genero, pais=pais)
    pelicula.save()
    return render(request, 'crear_pelicula.html', {'pelicula': pelicula})