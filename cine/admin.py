from django.contrib import admin
from .models import Genero, Pelicula, Ticket

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    pass

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    pass

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    pass
