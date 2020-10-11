from django.contrib import admin
from .models import *
# Register your models here.


class RequisitosAdmin(admin.ModelAdmin):
    list_display=("TipoRequisito",)
    search_fields=("TipoRequisito",)

class PeriodoAdmin(admin.ModelAdmin):
    list_display=("TipoPeriodo","Turnos")
    search_fields=("TipoPeriodo",)

class AfectaAdmin(admin.ModelAdmin):
    list_display=("TipoAfect",)
    search_fields=("TipoAfect",)

class EventoAdmin(admin.ModelAdmin):
    list_display=("Descripcion", "TipoEvento",)
    search_fields=("Descripcion",)
    list_filter=("TipoEvento",)
    exclude = ('User',)

class Evento_RequisitosAdmin(admin.ModelAdmin):
    list_display=("Evento", "Requisito", "Cantidad")
    search_fields=("Evento__Descripcion",)
    list_filter=("Requisito",)

class Evento_AfectaAdmin(admin.ModelAdmin):
    list_display=("Evento", "Afecta", "Cantidad","Periodo", "Duracion")
    search_fields=("Evento__Descripcion",)
    list_filter=("Afecta","Periodo")

class TipoEventoAdmin(admin.ModelAdmin):
    list_display=("TipoEvento",)
    search_fields=("TipoEvento",)

class PrestamoAdmin(admin.ModelAdmin):
    list_display=("Cantidad", "Intereses", "TipoPrestamo")
    search_fields=("Cantidad",)
    list_filter=("TipoPrestamo",)
    exclude = ('User',)

class Prestamo_RequisitosAdmin(admin.ModelAdmin):
    list_display=("Prestamo", "Requisito", "Cantidad")
    search_fields=("Prestamo__Cantidad",)
    list_filter=("Requisito",)

class Prestamo_AfectAdmin(admin.ModelAdmin):
    list_display=("Prestamo", "Afecta", "Cantidad","Periodo", "Duracion")
    search_fields=("Prestamo__Cantidad",)
    list_filter=("Afecta","Periodo")

class TipoPrestamoAdmin(admin.ModelAdmin):
    list_display=("TipoPrestamo",)
    search_fields=("TipoPrestamo",)

class PreguntasAdmin(admin.ModelAdmin):
    list_display=("Descripcion", "TipoPreguntas")
    search_fields=("Descripcion",)
    list_filter=("TipoPreguntas",)
    exclude = ('User',)

class Preguntas_RequisitosAdmin(admin.ModelAdmin):
    list_display=("Preguntas", "Requisito", "Cantidad")
    search_fields=("Preguntas__Descripcion",)
    list_filter=("Requisito",)

class Preguntas_AfectaAdmin(admin.ModelAdmin):
    list_display=("Preguntas", "Afecta", "Cantidad","Periodo", "Duracion")
    search_fields=("Preguntas__Descripcion",)
    list_filter=("Afecta","Periodo")

class TipoPreguntaAdmin(admin.ModelAdmin):
    list_display=("TipoPregunta",)
    search_fields=("TipoPregunta",)

class ArchivosAdmin(admin.ModelAdmin):
    fields = ["Archivo",]
    list_display = ("Archivo",)
    search_fields = ("Archivo",)

admin.site.register(Requisitos, RequisitosAdmin)
admin.site.register(Afecta, AfectaAdmin)
admin.site.register(Periodo, PeriodoAdmin)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Evento_Requisitos, Evento_RequisitosAdmin)
admin.site.register(Evento_Afecta, Evento_AfectaAdmin)
admin.site.register(TipoEvento, TipoEventoAdmin)

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Prestamo_Requisitos, Prestamo_RequisitosAdmin)
admin.site.register(Prestamo_Afect, Prestamo_AfectAdmin)
admin.site.register(TipoPrestamo, TipoPrestamoAdmin)

admin.site.register(Preguntas, PreguntasAdmin)
admin.site.register(Preguntas_Requisitos, Preguntas_RequisitosAdmin)
admin.site.register(Preguntas_Afecta, Preguntas_AfectaAdmin)
admin.site.register(TipoPregunta, TipoPreguntaAdmin)

admin.site.register(Archivos, ArchivosAdmin)

#admin.site.register(User)
#admin.site.register(Turnos)
#admin.site.register(Turnos_Requisitos)
#admin.site.register(Turnos_Afecta)



