from django.db import models
from django.urls import reverse

#DECLARACION DE MODELOS DE PRODUCTORA, POST Y CONTACTO PARA SQLITE
class Productora(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    nombre = models.CharField(max_length=100)
    productora  = models.ForeignKey(
        Productora,
        null=True,
        blank=True,
        on_delete = models.CASCADE,
    )
    descripcion = models.TextField()
    imagen = models.TextField(default='')
    año = models.IntegerField()

    def __str__(self):
        return self.nombre

def get_absolute_url(self):
        return reverse('peliculas', args=[str(self.id)])

#OPCIONES DE CONTACTO (TIPO)
opciones = [
    [0,"Consulta"],
    [1,"Queja"],
    [2,"Sugerencia"],
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo = models.IntegerField(choices=opciones)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
