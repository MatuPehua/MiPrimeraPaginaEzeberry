from django.urls import path
from inicio.views import inicio, crear_pelicula 

urlpatterns = [
    path('inicio/', inicio),
    path('peliculas/crear/', crear_pelicula),

]

# <pelicula>/<genero>/<pais>/