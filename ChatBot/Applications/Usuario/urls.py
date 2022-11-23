
from django.urls import path 

from . import views

app_name="usuarios_app"
urlpatterns = [
 path(
    'registro/',
    views.RegistroUsuarioCreateView.as_view(),
    name="registro-usuario",
    ),
 path(
    'login',
     views.LoginUser.as_view(),
     name="login-user"

 ),
    
path(
    'logout',
     views.CerrarSesionView.as_view(),
     name="Cerrar-user"

 )
]
