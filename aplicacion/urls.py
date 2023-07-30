from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="inicio" ),

#Paths de HTML
    path('peliculas/', peliculas, name="peliculas"),
    path('clientes/', clientes, name="clientes"),
    path('videojuegos/', videojuegos, name="videojuegos"),

#Paths de Forms
    path('videojuegosForm/', videojuegosForm, name="videojuegosForm"),
    path('clientesForm/', clientesForm, name="clientesForm"),
    path('peliculasForm/', peliculasForm, name="peliculasForm"),

#Paths de Buscadores
    path('buscarPelicula/', buscarPelicula, name="buscarPelicula"),
    path('buscar/', buscar, name="buscar"),
]