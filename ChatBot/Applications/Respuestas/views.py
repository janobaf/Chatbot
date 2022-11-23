from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .models import Respuestas

class CreacionRespuestasCreateView(LoginRequiredMixin,CreateView):
    model = Respuestas
    template_name = "respuestas/crear_respuestas.html"
    fields=('__all__')
    login_url = reverse_lazy('usuarios_app:login-user')

    success_url="."
# Create your views here.


