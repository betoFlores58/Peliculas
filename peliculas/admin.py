from django.contrib import admin
from .models import Post
from peliculas.models import Productora, Contacto

#Declaramos todos los modelos que estaremos utilizando
admin.site.register(Post)
admin.site.register(Productora)
admin.site.register(Contacto)