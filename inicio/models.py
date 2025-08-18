from django.db import models

class Peliculas(models.Model):
    pelicula=models.CharField(max_length=40)
    genero=models.CharField(max_length=40)
    pais=models.CharField(max_length=40)

    def __str__(self):
        return f'{self.pelicula} {self.genero} {self.pais}'
