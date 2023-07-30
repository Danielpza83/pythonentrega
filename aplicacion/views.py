from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def peliculas(request):
    ctx = {"peliculas": Peliculas.objects.all() }
    return render(request, "aplicacion/peliculas.html", ctx)

def videojuegos(request):
    ctx = {"videojuegos": Videojuegos.objects.all() }
    return render(request, "aplicacion/videojuegos.html", ctx)

def clientes(request):
    ctx = {"clientes": Clientes.objects.all() }
    return render(request, "aplicacion/clientes.html", ctx)


# Forms:

def videojuegosForm(request):
    if request.method == "POST":
        videojuegos_Form = VideojuegosForm(request.POST)
        print(videojuegos_Form)
        if videojuegos_Form.is_valid:
            informacion = videojuegos_Form.cleaned_data
            videojuegos = Videojuegos(
                titulo=informacion['titulo'],
                director=informacion['director'],
                productora=informacion['productora'],
                genero=informacion['genero'],
                fecha_estreno=informacion['fecha_estreno'],
                cantidad=informacion['cantidad'],
                consolas=informacion['consolas'],
            )
            videojuegos.save()
            return render(request, "aplicacion/base.html")
    else:
        videojuegos_Form = VideojuegosForm()
        return render(request, "aplicacion/videojuegosForm.html", {"form":videojuegos_Form})

def clientesForm(request):
    if request.method == "POST":
        clientes_Form = ClientesForm(request.POST)
        print(clientes_Form)
        if clientes_Form.is_valid:
            informacion = clientes_Form.cleaned_data
            clientes = Clientes(
                nombre=informacion['nombre'],
                apellido=informacion['apellido'],
                email=informacion['email'],
                direccion=informacion['direccion'],
            )
            clientes.save()
            return render(request, "aplicacion/base.html", {"form":clientes_Form})
    else:
        clientes_Form = ClientesForm()
        return render(request, "aplicacion/clientesForm.html", {"form":clientes_Form})

def peliculasForm(request):
    if request.method == "POST":
        peliculas_Form = PeliculasForm(request.POST)
        print(peliculas_Form)
        if peliculas_Form.is_valid:
            informacion = peliculas_Form.cleaned_data
            peliculas = Peliculas(
                titulo=informacion['titulo'],
                director=informacion['director'],
                productora=informacion['productora'],
                actor_protagonista=informacion['actor_protagonista'],
                genero=informacion['genero'],
                fecha_estreno=informacion['fecha_estreno'],
                cantidad=informacion['cantidad'],
            )
            peliculas.save()
            return render(request, "aplicacion/base.html", {"form":peliculas_Form})
    else:
        peliculas_Form = PeliculasForm()
        return render(request, "aplicacion/peliculasForm.html", {"form":peliculas_Form})


#Buscadores

def buscarPelicula(request):
    return render(request, "aplicacion/buscarPelicula.html")

def buscar(request):
    if request.GET['titulo']:
        titulo = request.GET['titulo']
        genero = Peliculas.objects.filter(titulo__icontains=titulo)
        return render(request, "aplicacion/resultadosPeliculas.html", 
                      {"titulo":titulo, 
                      "genero":genero}
                      )