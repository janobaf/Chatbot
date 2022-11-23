from django.db import models
from ..Respuestas.models import Respuestas
from .managers import Crear_preguntas
from django.conf import settings
# Create your models here.
class Pregunta(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pregunta = models.CharField(max_length=50)
    respuesta = models.ForeignKey(Respuestas, on_delete=models.CASCADE)
    objects=Crear_preguntas()