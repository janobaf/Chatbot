from django.urls import path 

from . import views

app_name="respuestas_app"
urlpatterns = [
 path(
    'addRespuestas/',
    views.CreacionRespuestasCreateView.as_view(),
    name="registrar-respuestas",
    ),

]
