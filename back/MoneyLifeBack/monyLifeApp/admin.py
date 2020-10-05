from django.contrib import admin
from .models import Preguntas, Tipo_Evento, Tipo_Pregunta, Tipo_Prestamo, Evento
# Register your models here.
admin.site.register(Preguntas)
admin.site.register(Tipo_Evento)
admin.site.register(Tipo_Pregunta)
admin.site.register(Tipo_Prestamo)
admin.site.register(Evento)
