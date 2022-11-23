from django.shortcuts import render 
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (View,ListView )
from ..Preguntas.models import Pregunta
from ..Respuestas.models import Respuestas
from ..bot import bot
from django.contrib.auth.mixins import LoginRequiredMixin

class inicioView(LoginRequiredMixin,ListView):
    template_name = "index/inicio.html"
    context_object_name="rpt"
    model=Pregunta
    login_url = reverse_lazy('usuarios_app:login-user')
    def get_queryset(self) :
        return Pregunta.objects.filtrar_users(self.request.user)

class preguntasView(View):
    def post(self,request,*args,**kwargs):
        if request.method =='POST':
            user=self.request.user
            print(user)
            pregunta = request.POST
            auxiliar=Respuestas.objects.all()
            i=bot.respuesta(auxiliar,pregunta['pregunta'])
            if i!=-1:
                if user!='AnonymousUser':
                    Pregunta.objects.crear_pregunta(user,pregunta['pregunta'],auxiliar[int(i)])
                else:
                    Pregunta.objects.crear_pregunta(user,pregunta['pregunta'],auxiliar[int(i)])

        
            return HttpResponseRedirect(
                reverse(
                    'inicio_app:inicio',
                )
            )


