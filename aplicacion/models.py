from django.db import models

# Create your models here.

generos_peliculas = (
    ("DRAMA", "Drama")
    ("ACCION", "Acción")
    ("AVENTURA", "Aventura")
    ("COMEDIA", "Comedia")
    ("TERROR", "Terror")
    ("OTROS", "Otros")
 )

generos_videojuegos = (
        ("FPS", "FPS")
        ("ACCION", "Acción")
        ("AVENTURA", "Aventura")
        ("ESTRATEGIA", "Estrategia")
        ("TERROR", "Terror")
        ("OTROS", "Otros")
    )


class peliculas(models.Model):
    
    titulo = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    productora = models.CharField(max_length=50)
    actor_protagonista = models.CharField(max_length=50)
    genero = models.CharField(max_length=20, choices=generos_peliculas)
    fecha_estreno = models.DateField()
    cantidad = models.IntegerField()



class videojuegos(models.Model):
    titulo = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    productora = models.CharField(max_length=50)
    genero = models.CharField(max_length=20, choices=generos_videojuegos)
    fecha_estreno = models.DateField()
    cantidad = models.IntegerField()

class clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=200)


