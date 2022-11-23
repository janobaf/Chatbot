from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.views.generic import (
    View,
    CreateView
)
from django.views.generic.edit import( FormView)
from .forms import FormularioRegistroForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import usuario
from django.urls import reverse_lazy,reverse

class RegistroUsuarioCreateView(FormView):
    template_name = 'usuarios/registro.html'
    form_class = FormularioRegistroForm
    success_url = reverse_lazy('usuarios_app:login-user')
    def form_valid(self, form) :
        usuario.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['password1'],
            nombre=form.cleaned_data['nombre'],
            imagen=form.cleaned_data['imagen'],
            
        )

        return super(RegistroUsuarioCreateView,self).form_valid(form)


class LoginUser(FormView):
    template_name = "usuarios/login.html"
    form_class = LoginForm
    success_url = reverse_lazy('inicio_app:inicio')

    def form_valid(self, form) :
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']

        )
        login(self.request,user)

        return super(LoginUser,self).form_valid(form)


class CerrarSesionView(View):
    
    def get(self, request,*args,**kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('usuarios_app:login-user')
        )