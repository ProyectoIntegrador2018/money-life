from django.contrib.auth.models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.renderers import JSONRenderer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only':True, 'required': True}}

    def create(self, validate_data): #validate_data es para hacer hash en la contraseña
        user = User.objects.create_user(**validate_data)
        
        #Crear turno actual del usuario
        newTurno = Turnos(NumeroTurnos=0, Felicidad=50, DineroEfectivo=20000, Ingresos=1000, Egresos=0, Sueldo=15000, User=user)
        newTurno.save()

        #Crear relacion con todos los eventos
        eventos = Evento.objects.all()
        for event in eventos:
            user_event = Evento_User(User=user, Evento=event, Frecuencia=event.Frecuencia, TipoEvento=event.TipoEvento)
            user_event.save()

        #Crear relacion con todas las preguntas
        preguntas = Preguntas.objects.all()
        for pregu in preguntas:
            user_pregu = Preguntas_User(User=user, Pregunta=pregu, Frecuencia=pregu.Frecuencia, TipoPreguntas=pregu.TipoPreguntas)
            user_pregu.save()
        
        #Crear afecta de sueldo
        user_afecta = Afecta_user(Afecta="SueldoReal", Descripcion="Eres empleado", User=user, TurnosEsperar=4, TurnosRestante=4, Cantidad=newTurno.Sueldo, Duracion=99999999)
        user_afecta.save()

        egreso_afecta = Afecta_user(Afecta="EgresoPersonal", Descripcion="Tienes hambre", User=user, TurnosEsperar=4, TurnosRestante=4, Cantidad=8000, Duracion=99999999)
        egreso_afecta.save()
        return user

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['id','Descripcion', 'TipoEvento']

class TurnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turnos
        fields = ['id','NumeroTurnos', 'Felicidad', 'DineroEfectivo', 'Ingresos', 'Egresos', 'Sueldo']

class PrestamosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPrestamo
        fields = ['id','TipoPrestamo', 'Duracion', 'TazaInteres']

class TipoInversionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInversiones
        fields = ['id','Inversion', 'TipoInversion', 'RangoRendimiento']

class InversionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inversion
        fields = ['id','NombreInversion', 'TipoEmpresa', 'SaldoInicial', 'SaldoAportacion', 'Aportacion', 'SaldoActual']

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = ['id','Descripcion', 'TipoPreguntas']

class PruebaSerializer(serializers.Serializer):
    EventoID = serializers.IntegerField()
    Descripcion = serializers.CharField(max_length=100)
    Periodo = serializers.CharField(max_length=50)
    Duracion = serializers.IntegerField()

class Prueba:
    def __init__(self, EventoID, Descripcion, Periodo, Duracion):
        self.EventoID = EventoID
        self.Descripcion = Descripcion
        self.Periodo = Periodo
        self.Duracion = Duracion


    