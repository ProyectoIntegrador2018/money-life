from django.db import models

# Create your models here.

#Crear tabla tipo de evento
class Tipo_Evento(models.Model):
    TipoEvento = models.CharField(max_length=30)

#Crear tabla de tipo de prestamo
class Tipo_Prestamo(models.Model):
    TipoPrestamo = models.CharField(max_length=30)

#Crear la tabla tipo de pregunta:
class Tipo_Pregunta(models.Model):
     TipoPregunta = models.CharField(max_length=30)

#Crear la tabla Usuario
class User(models.Model):
    RolUsuario = models.CharField(max_length=30)

#Crear la tabla EVENTO y sus relaciones
#---------------------------------------------------------------

#Crear tabla evento
class Evento(models.Model):
    Descripcion = models.CharField(max_length=200)
    Frecuencia = models.IntegerField()
    Probabilidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    TipoEvento = models.ForeignKey(Tipo_Evento, null=True ,on_delete = models.CASCADE)
    User = models.ForeignKey(User, null=True, on_delete = models.SET_NULL) #Relacion con User
    
    

#---------------------------------------------------------------

#Crear la tabla PRESTAMO y sus relaciones
#---------------------------------------------------------------

#Crear tabla Prestamo
class Prestamo(models.Model):
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    Intereses = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    TipoPrestamo = models.ForeignKey(Tipo_Prestamo, null=True ,on_delete=models.CASCADE)
    User = models.ForeignKey(User, null=True, on_delete = models.SET_NULL) #Relacion con User
    


#---------------------------------------------------------------

#Crear la tabla PREGUNTAS y sus relaciones
#---------------------------------------------------------------

#Crear tabla Preguntas
class Preguntas(models.Model):
    Descripcion = models.CharField(max_length=200)
    Probabilidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    TipoPregunta = models.ForeignKey(Tipo_Pregunta, null=True ,on_delete=models.CASCADE)
    User = models.ForeignKey(User, null=True, on_delete = models.SET_NULL) #Relacion con User
    
#---------------------------------------------------------------

#Crear tabla Turnos y sus relaciones
class Turnos(models.Model):
    NumeroTurnos = models.IntegerField()
    Felicidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    DineroEfectivo = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    Ingresos = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    Egresos = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    Edad = models.IntegerField()
    Sexo = models.CharField(max_length=10)
    User = models.ForeignKey(User, null=True, on_delete = models.SET_NULL) #Relacion con User
    Evento = models.ForeignKey(Evento, on_delete = models.CASCADE) #Relacion con Evento
    Prestamo = models.ForeignKey(Prestamo, on_delete = models.CASCADE) #Relacion con Prestamo
    Preguntas = models.ForeignKey(Preguntas, on_delete = models.CASCADE) #Relacion con Preguntas
