from django.contrib import admin
from .models import Genero, Pelicula, Ticket

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio_form", "disponibilidad", "fecha_estreno", "genero", "imagen")
    search_fields = ("nombre",)
    list_filter = ("genero",)
    list_editable = ("disponibilidad", "genero")

    def precio_form (self, obj):
        return f"${obj.precio:,}".replace("," , ".")

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("nombre", "correo", "cantidad", "fecha", "pelicula__nombre")
    list_filter = ("pelicula",)
