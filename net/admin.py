from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Netbook, Escuela, Informe, Actividad, Directivo, User


class NetbookAdmin(admin.ModelAdmin):
    list_display = ["escuela", "identificador", "serie", "estado"]
    list_editable = ["estado"]
    search_fields = ["estado"]
    list_filter = ["estado", "escuela"]
    list_per_page = 30


class EscuelaAdmin(admin.ModelAdmin):
    list_display = ["cuise", "cue", "nombre", "localidad", "direccion"]
    list_editable = ["direccion", "cue", "nombre"]
    search_fields = ["localidad",  "cue", "cuise"]
    list_filter = ["localidad"]
    list_per_page = 10


class InformeAdmin(admin.ModelAdmin):
    list_display = ["fecha", "autor", "escuela"]
    search_fields = ["fecha", "autor", "escuela"]
    list_filter = ["fecha", "autor", "escuela"]
    list_per_page = 10


class ActividadAdmin(admin.ModelAdmin):
    list_display = ["fecha", "autor"]
    search_fields = ["fecha", "autor"]
    list_filter = ["fecha", "autor"]
    list_per_page = 50


class DirectivoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "apellido", "dni", "telefono", "email"]
    search_fields = ["apellido", "dni", "telefono", "email"]
    list_filter = ["apellido", "dni", "email"]
    list_per_page = 50

    # Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Netbook, NetbookAdmin)
admin.site.register(Escuela, EscuelaAdmin)
admin.site.register(Informe, InformeAdmin)
admin.site.register(Actividad, ActividadAdmin)
admin.site.register(Directivo, DirectivoAdmin)
