from django.db import models

# Create your models here.

#Crear la tabla Requisitos
class Requisitos(models.Model):
    TipoRequisito = models.CharField(max_length=30)

#Crear la tabla Afecta
class Afecta(models.Model):
    TipoAfect = models.CharField(max_length=30)

#Crear la tabla Usuario
class User(models.Model):
    RolUsuario = models.CharField(max_length=30)

#Crear la tabla EVENTO y sus relaciones
#---------------------------------------------------------------

#Crear tabla evento
class Evento(models.Model):
    TipoEvento = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=200)
    Frecuencia = models.IntegerField()
    Probabilidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    Requisitos = models.ManyToManyField(Requisitos, through='Evento_Requisitos') #Relacion con Requisitos
    Afecta = models.ManyToManyField(Afecta, through='Evento_Afect') #Relacion con Afecta
    User = models.ForeignKey(User, on_delete = models.CASCADE) #Relacion con User
    

#Tabla relacion con Requisitos
class Evento_Requisitos(models.Model):
    id_Requisito = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    id_Evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['id_Requisito','id_Evento']]

#Tabla relacion con Afecta
class Evento_Afect(models.Model):
    id_Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    id_Evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['id_Afecta','id_Evento']]

#---------------------------------------------------------------

#Crear la tabla PRESTAMO y sus relaciones
#---------------------------------------------------------------

#Crear tabla Prestamo
class Prestamo(models.Model):
    TipoPrestamo = models.CharField(max_length=30)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    Intereses = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    Requisitos = models.ManyToManyField(Requisitos, through='Prestamo_Requisitos') #Relacion con Requisitos
    Afecta = models.ManyToManyField(Afecta, through='Prestamo_Afect') #Relacion con Afecta
    User = models.ForeignKey(User, on_delete = models.CASCADE) #Relacion con User

#Tabla relacion con Requisitos
class Prestamo_Requisitos(models.Model):
    id_Requisito = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    id_Prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    CantidadRecurente = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['id_Requisito','id_Prestamo']]

#Tabla relacion con Afecta
class Prestamo_Afect(models.Model):
    id_Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    id_Prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['id_Afecta','id_Prestamo']]

#---------------------------------------------------------------

#Crear la tabla PREGUNTAS y sus relaciones
#---------------------------------------------------------------

#Crear tabla Preguntas
class Preguntas(models.Model):
    TipoPregunta = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=200)
    Probabilidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)
    Requisitos = models.ManyToManyField(Requisitos, through='Preguntas_Requisitos') #Relacion con Requisitos
    Afecta = models.ManyToManyField(Afecta, through='Preguntas_Afecta') #Relacion con Afecta
    User = models.ForeignKey(User, on_delete = models.CASCADE) #Relacion con User

class Preguntas_Requisitos(models.Model):
    id_Requisito = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    id_Preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    CantidadRecurente = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['id_Requisito','id_Preguntas']]

class Preguntas_Afecta(models.Model):
    id_Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    id_Preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['id_Afecta','id_Preguntas']]

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
    Requisitos = models.ForeignKey(Requisitos, on_delete = models.CASCADE) #Relacion con Requisitos
    Afecta = models.ForeignKey(Afecta, on_delete = models.CASCADE) #Relacion con Afecta
    User = models.ForeignKey(User, on_delete = models.CASCADE) #Relacion con User
    Evento = models.ForeignKey(Evento, on_delete = models.CASCADE) #Relacion con Evento
    Prestamo = models.ForeignKey(Prestamo, on_delete = models.CASCADE) #Relacion con Prestamo
    Preguntas = models.ForeignKey(Preguntas, on_delete = models.CASCADE)
