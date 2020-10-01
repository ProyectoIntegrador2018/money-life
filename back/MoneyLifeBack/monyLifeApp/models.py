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
    Afecta = models.ManyToManyField(Afecta, through='Evento_Afecta') #Relacion con Afecta
    User = models.ForeignKey(User, null=True, on_delete = models.SET_NULL) #Relacion con User
    

#Tabla relacion con Requisitos
class Evento_Requisitos(models.Model):
    Requisito = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['Requisito','Evento']]

#Tabla relacion con Afecta
class Evento_Afecta(models.Model):
    Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['Afecta','Evento']]

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
    User = models.ForeignKey(User, null=True, on_delete = models.SET_NULL) #Relacion con User

#Tabla relacion con Requisitos
class Prestamo_Requisitos(models.Model):
    Requisito = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    Prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    CantidadRecurente = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['Requisito','Prestamo']]

#Tabla relacion con Afecta
class Prestamo_Afect(models.Model):
    Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    Prestamo = models.ForeignKey(Prestamo, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['Afecta','Prestamo']]

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
    User = models.ForeignKey(User, null=True, on_delete = models.SET_NULL) #Relacion con User

class Preguntas_Requisitos(models.Model):
    Requisito = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    Preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    CantidadRecurente = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['Requisito','Preguntas']]

class Preguntas_Afecta(models.Model):
    Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    Preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['Afecta','Preguntas']]

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

    Requisitos = models.ManyToManyField(Requisitos, through='Turnos_Requisitos') #Relacion con Requisitos
    Afecta = models.ManyToManyField(Afecta, through='Turnos_Afecta') #Relacion con Afecta

class Turnos_Requisitos(models.Model):
    Requisito = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    Turnos = models.ForeignKey(Turnos, on_delete=models.CASCADE)
    Cantidad= models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['Requisito','Turnos']]

class Turnos_Afecta(models.Model):
    Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    Turnos = models.ForeignKey(Turnos, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=10)

    class Meta:
        unique_together = [['Afecta','Turnos']]