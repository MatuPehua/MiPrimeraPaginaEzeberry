from django.db import models

class Peliculas(models.Model):
    nombre_pelicula=models.CharField(max_length=40)
    Genero=models.CharField(max_length=40)
    
