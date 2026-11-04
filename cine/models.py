from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

class Pelicula (models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    disponibilidad = models.BooleanField(default=False)
    fecha_estreno = models.DateField()
    genero = models.ForeignKey(
        Genero, 
        on_delete = models.CASCADE,
        related_name="peliculas",
    )
    imagen = models.ImageField(upload_to='peliculas/', blank=True, null=True)

class Ticket (models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    cantidad = models.PositiveSmallIntegerField()
    fecha = models.DateTimeField()
    pelicula = models.ForeignKey(
        Pelicula,
        on_delete=models.CASCADE,
        related_name="tickets",
    )
    