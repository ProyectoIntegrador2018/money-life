from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from decimal import Decimal
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
import re
import random

#Login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #authentication_classes = {TokenAuthentication,}
    #permission_classes = {IsAuthenticated,}

###################################################################
#LOGICA DE EVENTOS

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    #Se llama al inicio del turno
    @action(methods=['get'], detail=False)
    def inicioTurno(self, request):
        queryset = Evento.objects.all()
        serializer = EventoSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    #Se llama al final del turno
    @action(methods=['put'], detail=False) #se necesita el usuario
    def afectaTurno(self, request):
        modifyEvento(request.data) #Modifica la frcuencia del evento que se utilizo
        eventoAfecta(request.data) #Crea los afecta del evento que se utilizo

        queryset = Evento.objects.all()
        serializer = EventoSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

#Funciones que llaman los servicios de eventos
def modifyEvento(data):
    user = User.objects.filter(id = 3).first() #Esto son pruebas con el usuario
    print(user.id)

    
    for evento in data:
        changefrecuencia = Evento_User.objects.get(User=user.id, Evento=evento['id'])
        Evento_User.objects.filter(User=user.id, Evento=evento['id']).update(Frecuencia=changefrecuencia.Frecuencia - 1)
    

def eventoAfecta(data):
    print("ENTRO EN AFECTA")
    user = User.objects.filter(id = 3).first() #Esto son pruebas con el usuario
    for evento in data:
        afecta_evento = Evento_Afecta.objects.filter(Evento=evento['id'])
        for afecta in afecta_evento:
            duracion = Periodo.objects.filter(TipoPeriodo=afecta.Periodo).first()
            afecta_usuario = Afecta_user(User=user, Descripcion=evento.Descripcion, Afecta=afecta.Afecta, TurnosEsperar=duracion.Turnos, TurnosRestante=duracion.Turnos, Cantidad=afecta.Cantidad, Duracion=afecta.Duracion)
            afecta_usuario.save()

###################################################################

###################################################################
#LOGICA DE TURNOS

class TurnosViewSet(viewsets.ModelViewSet):
    queryset = Turnos.objects.all()
    serializer_class = TurnosSerializer

    #Este servicio se manda cada que inicie el turno
    @action(methods=['get', 'put'], detail=False)  #se necesita el usuario
    def inicio(self, request):

        #afectaTurnos() #Llama a todos los afecta que esten relacionados con el usuario y los aplica
        prestamosTurnos() #Llama a todos los prestamos relacionados con este usuario para aplicar el gasto
        #inversionesTurnos() #Llama a todas las inversiones relacionados con este usuario y aplica su flujo

        user = User.objects.filter(id = 3).first() #Esto son pruebas con el usuario
        queryset = Turnos.objects.filter(User=user)
        serializer = TurnosSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

#Se aplican todos los afectas relacionados con el usuario
def afectaTurnos():
    user = User.objects.filter(id = 3).first() #Esto son pruebas con el usuario
    turno = Turnos.objects.filter(User=user).first()
    
    afectaActions = Afecta_user.objects.filter(User=user)
    for afecta in afectaActions:
        afecta.TurnosRestante = afecta.TurnosRestante - 1
        afecta.save()
        if afecta.TurnosRestante <= 0:
            afecta.Duracion = afecta.Duracion - 1
            afecta.save()
            if afecta.Duracion <= 0:
                afecta.delete()
            else:
                if afecta.Cantidad[0] == '%':
                    cantidadAfecta = afecta.Cantidad[1:]
                    if cantidadAfecta[0] == '-':
                        cantidadAfecta = cantidadAfecta[1:]
                        modifyTurno(turno, afecta.Afecta, cantidadAfecta, True, False)
                    else:
                        modifyTurno(turno, afecta.Afecta, cantidadAfecta, True, True)
                else:
                    modifyTurno(turno, afecta.Afecta, afecta.Cantidad, False, True)
                afecta.TurnosRestante = afecta.TurnosEsperar
                afecta.save()
                turno.save()
                
#Es la forma en la que se modifica el turno actual del usuario (Se puede cambiar)   
def modifyTurno(turno, afecta, cantidad, porcentaje, suma):
    if afecta == 'Egresos':
        if porcentaje:
            if suma:
                turno.Egresos = turno.Egresos + (turno.Egresos * Decimal(cantidad))
                return True
            turno.Egresos = turno.Egresos - (turno.Egresos * Decimal(cantidad))
            return True
        turno.Egresos = turno.Egresos + Decimal(cantidad)
        return True
            
    elif afecta == 'Ingresos':
        if porcentaje:
            if suma:
                turno.Ingresos = turno.Ingresos + (turno.Ingresos * Decimal(cantidad))
                return True
            turno.Ingresos = turno.Ingresos - (turno.Ingresos * Decimal(cantidad))
            return True
        turno.Ingresos = turno.Ingresos + Decimal(cantidad)
        return True

    elif afecta == 'Felicidad':
        if porcentaje:
            if suma:
                turno.Felicidad = turno.Felicidad + (turno.Felicidad * Decimal(cantidad))
                return True
            turno.Felicidad = turno.Felicidad - (turno.Felicidad * Decimal(cantidad))
            return True
        turno.Felicidad = turno.Felicidad + Decimal(cantidad)
        return True

    elif afecta == 'DineroEfectivo':
        if porcentaje:
            if suma:
                turno.DineroEfectivo = turno.DineroEfectivo + (turno.DineroEfectivo * Decimal(cantidad))
                return True
            turno.DineroEfectivo = turno.DineroEfectivo - (turno.DineroEfectivo * Decimal(cantidad))
            return True
        turno.DineroEfectivo = turno.DineroEfectivo + Decimal(cantidad)
        return True

def prestamosTurnos():
    user = User.objects.filter(id = 2).first() #Esto son pruebas con el usuario
    turno = Turnos.objects.filter(User=user).first()
    prestamos = Prestamo.objects.filter(User=user)

    for prestamo in prestamos:
        print("prestamo=",prestamo)
        turno.DineroEfectivo = turno.DineroEfectivo - prestamo.Mensualidad
        tipoPrestamo = prestamo.idPrestamo
        print(tipoPrestamo)
        
        tipoPrestamo = TipoPrestamo.objects.filter(idPrestamo = str(tipoPrestamo)).first()

        prestamo.SaldoAbsoluto = prestamo.SaldoAbsoluto - prestamo.Mensualidad

        if prestamo.SaldoAbsoluto < prestamo.Mensualidad:
            prestamo.Mensualidad = prestamo.SaldoAbsoluto

        interes = re.sub('%', '',str(tipoPrestamo.TazaInteres) )
        interes = float(interes)/100
        interesMensual = prestamo.SaldoAbsoluto * Decimal(interes/12)

        prestamo.Interes = interesMensual
        prestamo.save()

        if prestamo.SaldoAbsoluto <= 0:
            prestamo.delete()

        turno.save()

###################################################################

###################################################################

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = TipoPrestamo.objects.all()
    serializer_class = PrestamosSerializer


    @action(methods=['get'], detail=False)
    def catalogo(self, request):
        queryset = TipoPrestamo.objects.all()
        serializer = PrestamosSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    @action(methods=['put'], detail=False)
    def Realizar(self, request):

        jsonPrestamo = request.data

        minimoAprobatorio = jsonPrestamo["ValorTotal"] * .10

        if jsonPrestamo["Enganche"] < minimoAprobatorio:
            return JsonResponse({"error": "El enganche no puede ser menor al 10 porciento del valor total"}, safe=False)

        if jsonPrestamo["Enganche"] >= jsonPrestamo["ValorTotal"]:
            return JsonResponse({"error": "El enganche es mayor al prestamo pedido"}, safe=False)

        user = User.objects.filter(id = jsonPrestamo["UserID"]).first()
        turno = Turnos.objects.filter(User=user).first()
        tipoPrestamo = TipoPrestamo.objects.filter(idPrestamo = jsonPrestamo["PrestamoID"]).first()
        cantidadPrestada = jsonPrestamo["ValorTotal"] - jsonPrestamo["Enganche"]

        interes = re.sub('%', '',str(tipoPrestamo.TazaInteres) )
        interes = float(interes)/100
        anos = (tipoPrestamo.Duracion).split(" ")
        anos = int(anos[0])
        pagoMensual = cantidadPrestada/((1 - (pow((1 + (interes/12)), (-(anos*12)))))/(interes/12))
        interesMensual = cantidadPrestada*(interes/12)
        print(pagoMensual)
        print(interesMensual)

        if turno.Ingresos < pagoMensual:
            return JsonResponse({"error": "No cuentas con los ingresos necesarios para realizar este pedido"}, safe=False)

        prestamoUser = Prestamo(User=user, idPrestamo=tipoPrestamo, ValorTotal=jsonPrestamo["ValorTotal"], CantidadPrestada=cantidadPrestada, Enganche=jsonPrestamo["Enganche"], Frecuencia=4, Amortizacion=0, Interes=interesMensual, Mensualidad=pagoMensual, AbonoCapital=0, SaldoAbsoluto=cantidadPrestada )
        prestamoUser.save()

        return JsonResponse({}, safe=False)

    @action(methods=['put'], detail=False)
    def Amortizacion(self, request):

        jsonPrestamo = request.data

        user = User.objects.filter(id = jsonPrestamo["UserID"]).first()
        prestamo = Prestamo.objects.filter(id = jsonPrestamo["PrestamoID"], User = user).first()

        if prestamo.SaldoAbsoluto < jsonPrestamo["Amortizacion"]:
            return JsonResponse({"error": "El saldo absoluto es menos que la amortización"}, safe=False)

        prestamo.AbonoCapital = jsonPrestamo["Amortizacion"] + prestamo.AbonoCapital

        prestamo.SaldoAbsoluto = prestamo.SaldoAbsoluto - jsonPrestamo["Amortizacion"]

        if prestamo.SaldoAbsoluto < prestamo.Mensualidad:
            prestamo.Mensualidad = prestamo.SaldoAbsoluto

        prestamo.save()

        if prestamo.SaldoAbsoluto <= 0:
            prestamo.delete()
        
        return JsonResponse({}, safe=False)

###################################################################

###################################################################
class InversionViewSet(viewsets.ModelViewSet):
    queryset = TipoInversiones.objects.all()
    serializer_class = TipoInversionesSerializer

    @action(methods=['get'], detail=False)
    def catalogoDisponibles(self, request):

        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        actuales = Inversion.objects.filter(User=user)
        catalogo = TipoInversiones.objects.all()

        for inversionActual in actuales:
            catalogo = catalogo.exclude(id=inversionActual.TipoInversion.id)

        queryset = catalogo
        serializer = TipoInversionesSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    @action(methods=['get'], detail=False)
    def inversinesActuales(self, request):

        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        actuales = Inversion.objects.filter(User=user)

        queryset = actuales
        serializer = InversionesSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    @action(methods=['post'], detail=False)
    def nueva(self, request):

        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        compania = TipoInversiones.objects.filter(id=jsonInversion["InversionID"]).first()

        rangoRendimiento = (compania.RangoRendimiento).split(" ")

        limite_inferior = float(rangoRendimiento[0])
        limite_superior = float(rangoRendimiento[2])

        tasaRendimiento = random.uniform(limite_inferior,limite_superior)

        nuvaInversion = Inversion(User=user,TipoInversion=compania,NombreInversion=compania.Inversion,TipoEmpresa=compania.TipoInversion,SaldoInicial=jsonInversion['Cantidad'],SaldoAportacion=jsonInversion['Cantidad'],EventoExterno=0,TasaRendimiento=tasaRendimiento,Aportacion=0,SaldoActual=jsonInversion['Cantidad'])
        nuvaInversion.save()

        return JsonResponse({}, safe=False)

    @action(methods=['put'], detail=False)
    def agregarDinero(self, request):

        jsonInversion = request.data
        inversion = Inversion.objects.filter(id=jsonInversion["InversionID"]).first()

        inversion.SaldoAportacion = inversion.SaldoAportacion + jsonInversion["Cantidad"]
        inversion.SaldoActual = inversion.SaldoActual + jsonInversion["Cantidad"]
        inversion.save()
        
        return JsonResponse({}, safe=False)

    @action(methods=['put'], detail=False)
    def retirarDinero(self, request):
        
        jsonInversion = request.data
        inversion = Inversion.objects.filter(id=jsonInversion["InversionID"]).first()

        if jsonInversion["Cantidad"] >= inversion.SaldoActual:
            return JsonResponse({"error":"No cuentas con suficiente dinero para retirar esta cantidad"}, safe=False)

        inversion.Aportacion = inversion.Aportacion + jsonInversion["Cantidad"]
        inversion.SaldoActual = inversion.SaldoActual - jsonInversion["Cantidad"]
        inversion.save()
        
        return JsonResponse({}, safe=False)

    @action(methods=['put'], detail=False)
    def retirarAccion(self, request):
        
        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        turno = Turnos.objects.filter(User=user).first()
        inversion = Inversion.objects.filter(id=jsonInversion["InversionID"]).first()

        turno.DineroEfectivo = turno.DineroEfectivo + inversion.SaldoActual
        inversion.delete()
        turno.save()
        
        return JsonResponse({}, safe=False)

###################################################################

###################################################################

class PruebaViewSet(viewsets.ViewSet):

    @action(methods=['get'], detail=False)
    def prueba2(self, request):
        print("ENTRO A PRUEBA 2")
        pru = Prueba(EventoID=1, Descripcion="Prueba1", Periodo="Semana", Duracion=10)
        print(pru)
        serializer = PruebaSerializer(pru)
        return JsonResponse(serializer.data, safe=False)
    