from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'inicio.html')

def crear_pelicula(request, pelicula, genero, pais):
    return render(request, 'crear_pelicula.html')