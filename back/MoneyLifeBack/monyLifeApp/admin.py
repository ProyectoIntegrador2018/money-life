from django.contrib import admin
from .models import *
# Register your models here.

admin.autodiscover()
admin.site.enable_nav_sidebar = False

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

class PreguntasAdmin(admin.ModelAdmin):
    list_display=("Descripcion","Probabilidad", "TipoPreguntas")
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
    list_display=("TipoPregunta", "TasaRendimiento", "SaldoInversion")
    search_fields=("TipoPregunta",)

class ArchivosAdmin(admin.ModelAdmin):
    fields = ["Archivo",]
    list_display = ("Archivo",)
    search_fields = ("Archivo",)

class TipoInversionesAdmin(admin.ModelAdmin):
    list_display = ("Inversion", "TipoInversion", "RangoRendimiento")
    search_fields=("Inversion",)
    list_filter=("TipoInversion",)


class TipoPrestamoAdmin(admin.ModelAdmin):
    list_display = ("idPrestamo", "TipoPrestamo", "Duracion", "TazaInteres")
    list_filter=("TipoPrestamo",)

class TipoPrestamo_AfectAdmin(admin.ModelAdmin):
    list_display = ("TipoPrestamo", "Afecta", "Periodo", "Cantidad", "Duracion")
    list_filter=("TipoPrestamo",)


"""
TipoInversiones
Inversion
Inversion_Afecta
TipoPrestamo
Prestamo
Prestamo_Afect
"""

admin.site.register(Requisitos, RequisitosAdmin)
admin.site.register(Afecta, AfectaAdmin)
admin.site.register(Periodo, PeriodoAdmin)

admin.site.register(Evento, EventoAdmin)
admin.site.register(Evento_Requisitos, Evento_RequisitosAdmin)
admin.site.register(Evento_Afecta, Evento_AfectaAdmin)
admin.site.register(TipoEvento, TipoEventoAdmin)

admin.site.register(Preguntas, PreguntasAdmin)
admin.site.register(Preguntas_Requisitos, Preguntas_RequisitosAdmin)
admin.site.register(Preguntas_Afecta, Preguntas_AfectaAdmin)
admin.site.register(TipoPregunta, TipoPreguntaAdmin)

admin.site.register(TipoInversiones, TipoInversionesAdmin)

admin.site.register(TipoPrestamo, TipoPrestamoAdmin)

admin.site.register(TipoPrestamo_Afect, TipoPrestamo_AfectAdmin)

admin.site.register(Archivos, ArchivosAdmin)


#admin.site.register(User)
#admin.site.register(Turnos)
#admin.site.register(Turnos_Requisitos)
#admin.site.register(Turnos_Afecta)



