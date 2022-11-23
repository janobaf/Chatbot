from django.urls import path
from . import views

app_name="inicio_app"
urlpatterns=[
    path('',
        views.inicioView.as_view(),
        name="inicio"
    ),
    path('pregunta/',
        views.preguntasView.as_view(),
        name="pregunta"
    )

]