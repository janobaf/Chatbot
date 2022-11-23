from django.db import models
class Crear_preguntas(models.Manager):
    def _crearPreguntas(self,usuario,pregunta,respuesta):
        p=self.model(
            user=usuario,
            pregunta=pregunta,
            respuesta=respuesta
        )
        p.save(using=self.db)
        return p
    def crear_pregunta(self,usuario,pregunta,respuesta):
        return self._crearPreguntas(usuario=usuario,pregunta=pregunta,respuesta=respuesta)

    def filtrar_users(self,user):
        return self.filter(user=user)