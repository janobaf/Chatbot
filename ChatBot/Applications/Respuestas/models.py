from django.db import models

# Create your models here.

class Respuestas(models.Model):
    respuesta = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to="imagenes",blank=True)
    musica = models.FileField(upload_to="mp3",max_length=250,blank=True)