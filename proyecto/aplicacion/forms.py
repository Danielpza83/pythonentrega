from django import forms


class ClientesForm(forms.Form):
    nombre = forms.CharField(label="Inserte su Nombre", max_length=50, required=True)
    apellido = forms.CharField(label="Inserte su Apellido", max_length=50, required=True)
    email = forms.EmailField(label="Inserte su Email", max_length=50, required=True)
    direccion = forms.CharField(label="Inserte su Dirección", max_length=200, required=False)

class PeliculasForm(forms.Form):
        titulo = forms.CharField(label="Titulo", max_length=50, required=True)
        director = forms.CharField(label="Director", max_length=50, required=False)
        productora = forms.CharField(label="Productora", max_length=50, required=False)
        actor_protagonista = forms.CharField(label="Protagonista", max_length=50, required=True)
        generos_peliculas = (
            ("DRAMA", "Drama"),
            ("ACCION", "Acción"),
            ("AVENTURA", "Aventura"),
            ("COMEDIA", "Comedia"),
            ("TERROR", "Terror"),
            ("OTROS", "Otros"),
        )
        genero = forms.ChoiceField(label="Genero", choices=generos_peliculas, required=True)
        fecha_estreno = forms.DateField(label="Fecha de Estreno", required=False)
        cantidad = forms.IntegerField(label="Cantidad", required=True)

class VideojuegosForm(forms.Form):
        titulo = forms.CharField(label="Titulo", max_length=50, required=True)
        director = forms.CharField(label="Director", max_length=50, required=False)
        productora = forms.CharField(label="Productora", max_length=50, required=False)
        generos_videojuegos = (
            ("FPS", "FPS"),
            ("ACCION", "Acción"),
            ("AVENTURA", "Aventura"),
            ("ESTRATEGIA", "Estrategia"),
            ("TERROR", "Terror"),
            ("OTROS", "Otros"),
        )
        genero = forms.ChoiceField(label="Genero", choices=generos_videojuegos, required=True)
        fecha_estreno = forms.DateField()
        cantidad = forms.IntegerField(label="Cantidad", required=True)
        nombres_consolas = (
            ("PLAYSTATION_4", "PlayStation 4"),
            ("PLAYSTATION_5", "PlayStation 5"),
            ("NINTENDO_SWITCH", "Nintendo Switch"),
            ("XBOX_ONE", "Xbox One"),
            ("PC", "PC"),
            ("OTROS", "Otros"),
        )
        consolas = forms.ChoiceField(label="Consola", choices=nombres_consolas, required=True)



