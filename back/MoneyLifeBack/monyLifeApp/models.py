from django.db import models


# Create your models here.

class Archivos(models.Model):
    Archivo = models.FileField(upload_to='Files/')


    class Meta:
        verbose_name_plural = "Archivos"
    

#Crear la tabla Requisitos
class Requisitos(models.Model):
    TipoRequisito = models.CharField(max_length=30, verbose_name="Tipo Requisito")

    class Meta:
        verbose_name_plural = "Requisitos"

    def __str__(self):
        return self.TipoRequisito

#Crear la tabla Afecta
class Afecta(models.Model):
    TipoAfect = models.CharField(max_length=30, verbose_name="Tipo Afecta")

    class Meta:
        verbose_name_plural = "Afecta"

    def __str__(self):
        return self.TipoAfect

#Crear la tabla Usuario
class User(models.Model):
    RolUsuario = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "Usuario"

    def __str__(self):
        return self.RolUsuario

#Crear tabla Periodo
class Periodo(models.Model):
    TipoPeriodo = models.CharField(max_length=30)
    Turnos = models.IntegerField()

    class Meta:
        verbose_name_plural = "Periodo"

    def __str__(self):
        return self.TipoPeriodo

#Crear la tabla Tipo Evento
class TipoEvento(models.Model):
    TipoEvento = models.CharField(max_length=30, verbose_name="Tipo Evento")

    class Meta:
        verbose_name_plural = "Tipo Evento"

    def __str__(self):
        return self.TipoEvento

#Crear la tabla EVENTO y sus relaciones
#---------------------------------------------------------------

#Crear tabla evento
class Evento(models.Model):
    Descripcion = models.CharField(max_length=200)
    Frecuencia = models.IntegerField()
    Probabilidad = models.DecimalField(max_digits=20,  decimal_places=2)
    Requisitos = models.ManyToManyField(Requisitos, through='Evento_Requisitos') #Relacion con Requisitos
    Afecta = models.ManyToManyField(Afecta, through='Evento_Afecta') #Relacion con Afecta
    User = models.ForeignKey(User, blank=True, null=True, on_delete = models.SET_NULL) #Relacion con User
    TipoEvento = models.ForeignKey(TipoEvento,blank=True, null=True, on_delete = models.SET_NULL, verbose_name="Tipo Evento") #Relacion con TipoEvento

    class Meta:
        verbose_name_plural = "Eventos"
    
    def __str__(self):
        return self.Descripcion

#Tabla relacion con Requisitos
class Evento_Requisitos(models.Model):
    Requisito = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    Cantidad = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        unique_together = [['Requisito','Evento']]
        verbose_name_plural = "Evento_Requisito"

#Tabla relacion con Afecta
class Evento_Afecta(models.Model):
    Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    Evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    Periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    Cantidad = models.CharField(max_length=40, blank=True, null=True)
    Duracion = models.IntegerField()

    class Meta:
        unique_together = [['Afecta','Evento']]
        verbose_name_plural = "Evento_Afecta"

#---------------------------------------------------------------
#Crear la tabla Tipo Inversion
class TipoInversiones(models.Model):
    Inversion = models.CharField(max_length=40, blank=True, null=True)
    TipoInversion = models.CharField(max_length=40,blank=True, null=True)
    RangoRendimiento = models.CharField(max_length=40,blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tipo Inversion"

    def __str__(self):
        return self.TipoInversion
#---------------------------------------------------------------
#Crear la tabla Ultima Instancia Inversion
class Inversion(models.Model):
    TipoInversion = models.ForeignKey(TipoInversiones, on_delete=models.CASCADE)
    NombreInversion = models.CharField(max_length=40, blank=True, null=True)
    TipoEmpresa = models.CharField(max_length=40,blank=True, null=True)
    SaldoInicial = models.DecimalField(max_digits=20,decimal_places=2,blank=True, null=True)
    SaldoAportacion = models.DecimalField(max_digits=20,decimal_places=2,blank=True, null=True)
    EventoExterno = models.CharField(max_length=40, blank=True, null=True)
    TasaRendimiento = models.CharField(max_length=40, blank = True, null = True)
    Aportacion = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)
    SaldoActual = models.DecimalField(max_digits=20, decimal_places=2,blank=True, null=True)
    User = models.ForeignKey(User,blank=True, null=True, on_delete = models.SET_NULL) #Relacion con User

    class Meta:
        verbose_name_plural = "Inversion"

    def __str__(self):
        return self.NombreInversion

#---------------------------------------------------------------
#Crear la tabla Tipo Prestamo
class TipoPrestamo(models.Model):
    idPrestamo = models.IntegerField()
    TipoPrestamo = models.CharField(max_length=30, verbose_name="Tipo Prestamo")
    Duracion = models.CharField(max_length=30, verbose_name="Duración")
    TazaInteres = models.CharField(max_length=30, verbose_name="Taza de Interes")
    Afecta = models.ManyToManyField(Afecta, through='TipoPrestamo_Afect') #Relacion con Afecta

    class Meta:
        verbose_name_plural = "Tipo Prestamo"

    def __str__(self):
        return str(self.idPrestamo)

#Crear la tabla PRESTAMO y sus relaciones
#---------------------------------------------------------------
####ERRROR EN LA TABLA TIPO PRESTAMO Y CONEXIONES
#Crear tabla Prestamo
class Prestamo(models.Model):
    idPrestamo = models.ForeignKey(TipoPrestamo,blank=True, null=True, on_delete = models.SET_NULL, verbose_name="Tipo Prestamo") #Relacion con Prestamo
    User = models.ForeignKey(User, null=True, on_delete = models.SET_NULL) #Relacion con User
    ValorTotal = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    CantidadPrestada = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    Enganche = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    Amortizacion = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    Interes = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    Mensualidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    AbonoCapital = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    SaldoAbsoluto = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    

    class Meta:
        verbose_name_plural = "Prestamos"

    def __str__(self):
        return str(self.CantidadPrestada)


#Tabla relacion con Afecta
class TipoPrestamo_Afect(models.Model):
    Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    TipoPrestamo = models.ForeignKey(TipoPrestamo, on_delete=models.CASCADE)
    Periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    Cantidad = models.CharField(max_length=40, blank=True, null=True)
    Duracion = models.IntegerField()

    class Meta:
        unique_together = [['Afecta','TipoPrestamo']]
        verbose_name_plural = "Prestamo_Afecta"

#---------------------------------------------------------------

#Crear la tabla Tipo Pregunta
class TipoPregunta(models.Model):
    TipoPregunta = models.CharField(max_length=30, verbose_name="Tipo Pregunta")
    TasaRendimiento = models.CharField(max_length=30,verbose_name="Tasa de Rendimiento")
    SaldoInversion = models.CharField(max_length=30,verbose_name="Saldo de Inversion")

    class Meta:
        verbose_name_plural = "Tipo Pregunta"

    def __str__(self):
        return self.TipoPregunta

#Crear objeto pregunta
class InversionPregunta(models.Model):
    TipoInversion = models.ForeignKey(TipoPregunta, on_delete = models.CASCADE)
    SaldoInicial = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    InicialMasAportacion = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    EventoExterno = models.CharField(max_length=30)
    TazaRendimiento = models.CharField(max_length=30)
    Aportacion = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    SaldoActual = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    SaldoInvercion = models.CharField(max_length=30)

#Crear la tabla PREGUNTAS y sus relaciones
#---------------------------------------------------------------

#Crear tabla Preguntas
class Preguntas(models.Model):
    Descripcion = models.CharField(max_length=200)
    Probabilidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    Requisitos = models.ManyToManyField(Requisitos, through='Preguntas_Requisitos') #Relacion con Requisitos
    Afecta = models.ManyToManyField(Afecta, through='Preguntas_Afecta') #Relacion con Afecta
    User = models.ForeignKey(User, null=True, on_delete = models.SET_NULL) #Relacion con User
    TipoPreguntas = models.ForeignKey(TipoPregunta, on_delete = models.CASCADE, verbose_name="Tipo Pregunta") #Relacion con TipoPreguntas

    class Meta:
        verbose_name_plural = "Preguntas"

    def __str__(self):
        return self.Descripcion

class Preguntas_Requisitos(models.Model):
    Requisito = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    Preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    Cantidad = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        unique_together = [['Requisito','Preguntas']]
        verbose_name_plural = "Pregunta_Requisito"

class Preguntas_Afecta(models.Model):
    Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    Preguntas = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    Periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    Cantidad = models.CharField(max_length=40, blank=True, null=True)
    Duracion = models.IntegerField()

    class Meta:
        unique_together = [['Afecta','Preguntas']]
        verbose_name_plural = "Pregunta_Afecta"

#---------------------------------------------------------------

#Crear tabla Turnos y sus relaciones
class Turnos(models.Model):
    NumeroTurnos = models.IntegerField()
    Felicidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    DineroEfectivo = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    Ingresos = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    Egresos = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)
    Edad = models.IntegerField()
    Sexo = models.CharField(max_length=10)
    User = models.ForeignKey(User, null=True, on_delete = models.SET_NULL) #Relacion con User
    Evento = models.ForeignKey(Evento, on_delete = models.CASCADE) #Relacion con Evento
    Preguntas = models.ForeignKey(Preguntas, on_delete = models.CASCADE) #Relacion con Preguntas
    Requisitos = models.ManyToManyField(Requisitos, through='Turnos_Requisitos') #Relacion con Requisitos
    Afecta = models.ManyToManyField(Afecta, through='Turnos_Afecta') #Relacion con Afecta

    class Meta:
        verbose_name_plural = "Turnos"

    def __str__(self):
        return self.NumeroTurnos

class Turnos_Requisitos(models.Model):
    Requisito = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    Turnos = models.ForeignKey(Turnos, on_delete=models.CASCADE)
    Cantidad= models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)

    class Meta:
        unique_together = [['Requisito','Turnos']]
        verbose_name_plural = "Turno_Requisito"

class Turnos_Afecta(models.Model):
    Afecta = models.ForeignKey(Afecta, on_delete=models.CASCADE)
    Turnos = models.ForeignKey(Turnos, on_delete=models.CASCADE)
    Cantidad = models.DecimalField(blank=True, null=True, max_digits=20,  decimal_places=2)

    class Meta:
        unique_together = [['Afecta','Turnos']]
        verbose_name_plural = "Turno_Requisito"





