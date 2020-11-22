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
import json
import re
import random
import math
#Login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from monyLifeApp import scripts


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #authentication_classes = {TokenAuthentication,}
    #permission_classes = {IsAuthenticated,}

    @action(methods=['get', 'post'], detail=False)
    def login(self, request):
        print("Entro =",request.data)
        print("ENTRO A GET LOGIN")
        userData = request.data
        user = authenticate(username=userData['username'], password=userData['password'])
        if user == None:
            return JsonResponse({'mensaje': "Usuario o contrasena incorrecta"}, safe = False)
        return JsonResponse({'id': user.id, 'username': user.username}, safe = False)


###################################################################
#LOGICA DE EVENTOS

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    #Se llama al inicio del turno
    @action(methods=['get', 'post'], detail=False)
    def inicioTurno(self, request):
        print("ENTROOOOO EVENTO INICIOOOO TURNOOOO")
        print("ME LLEGO = ",request.data)
        jsonUser = request.data
        user = User.objects.filter(id = jsonUser['UserID']).first() 
        turno = Turnos.objects.filter(User=user).first()
        eventos = scripts.seleccionEvento(user)
        output = json.dumps(eventos)
        response = json.loads(output)
        scripts.getAfectaEvento(response)
        scripts.modifyEvento(user, response) #Modifica la frcuencia del evento que se utilizo
        afectaList = scripts.eventoAfecta(user, response) #Crea los afecta del evento que se utilizo
        afectaEventos = Afecta_user.objects.filter(id__in=afectaList)
        scripts.afectaTurnoinstantaneo(afectaEventos, turno)

        print("TE ENVIE",response)
        return JsonResponse(response, safe = False)

###################################################################

###################################################################
class PreguntaViewSet(viewsets.ModelViewSet):
    queryset = Preguntas.objects.all()
    serializer_class = PreguntasSerializer

    @action(methods=['get', 'post'], detail=False)
    def getPreguntas(self, request):
        print("ENTROOOOO PREGUNTA INICIOOOO TURNOOOO")
        print("ME LLEGO = ",request.data)
        jsonUser = request.data
        user = User.objects.filter(id = jsonUser['UserID']).first()

        preguntas = scripts.seleccionPregunta(user)
        output = json.dumps(preguntas)
        response = json.loads(output)
        scripts.getAfectaPregunta(response)
        print("TE ENVIE",response)
        return JsonResponse(response, safe = False)

    @action(methods=['put'], detail=False)
    def afectaPreguntas(self, request):
        print("ENTROOOOO PREGUNTA AFECTA INICIOOOO TURNOOOO")
        print("ME LLEGO PREGUNTA AFECTA = ",request.data)
        jsonPregunta = request.data
        
        user = User.objects.filter(id = jsonPregunta['UserID']).first()
        turno = Turnos.objects.filter(User=user).first()
        pregunta = Preguntas.objects.filter(id = jsonPregunta['PreguntaID']).first()
        
        if scripts.validarPregunta(user, pregunta):
            scripts.modifyPregunta(user, pregunta) #Modifica la frcuencia de la pregunta que se utilizo
            afectaList = scripts.preguntaAfecta(user, pregunta)
            afectasPregunta = Afecta_user.objects.filter(id__in=afectaList)
            scripts.afectaTurnoinstantaneo(afectasPregunta, turno)
        else:
            print("TE ENVIE ",{"mensaje":"No cuentas con los requisitos necesarios para esta accion"})
            return JsonResponse({"mensaje":"No cuentas con los requisitos necesarios para esta accion"}, safe=False)

        if turno.Felicidad >= Decimal(100):
            turno.Felicidad = Decimal(99.9)

        queryset = Turnos.objects.filter(User=user)
        serializer = TurnosSerializer(queryset, many=True)
        print("TE ENVIE",serializer.data)
        return JsonResponse(serializer.data, safe=False)



###################################################################

###################################################################
#LOGICA DE TURNOS

class TurnosViewSet(viewsets.ModelViewSet):
    queryset = Turnos.objects.all()
    serializer_class = TurnosSerializer

    #Este servicio se manda cada que inicie el turno
    @action(methods=['get', 'post'], detail=False)  #se necesita el usuario
    def inicio(self, request):
        print("ENTROOOOO INICIOOOO TURNOOOO")
        print("ME LLEGO = ",request.data)
        
        jsonTurno = request.data
        user = User.objects.filter(id = jsonTurno["UserID"]).first()
        turno = Turnos.objects.filter(User=user).first()
        prestamos = Prestamo.objects.filter(User=user)
        inversiones = Inversion.objects.filter(User=user)
        inversionesPregunta = InversionPregunta.objects.filter(User = user)

        scripts.afectaTurnos(user, turno) #Llama a todos los afecta que esten relacionados con el usuario y los aplica
        scripts.prestamosTurnos(user, turno, prestamos) #Llama a todos los prestamos relacionados con este usuario para aplicar el gasto
        scripts.inversionesTurnos(user, turno, inversiones) #Llama a todas las inversiones relacionados con este usuario y aplica su flujo
        scripts.inversionesPreguntasTurnos(user, turno, inversionesPregunta)
        scripts.turnoIngresosEgresos(user, turno) #Calcula los ingresos y egresos mensuales de este turno

        sueldoActual = Afecta_user.objects.filter(User=user, Afecta='SueldoReal').first()
        turno.Sueldo = Decimal(sueldoActual.Cantidad)
        turno.NumeroTurnos = turno.NumeroTurnos + 1
        if turno.Felicidad >= Decimal(100):
            turno.Felicidad = Decimal(99.9)
        turno.save()

        queryset = Turnos.objects.filter(User=user)
        serializer = TurnosSerializer(queryset, many=True)
        print("TE ENVIE",serializer.data)
        return JsonResponse(serializer.data, safe=False)

    @action(methods=['get', 'post'], detail=False)  #se necesita el usuario
    def intermedio(self, request):
        print("ENTROOOOO TURNOOOO INTERMEDIO")
        print("ME LLEGO = ",request.data)
        jsonTurno = request.data
        user = User.objects.filter(id = jsonTurno["UserID"]).first()
        turno = Turnos.objects.filter(User=user).first()

        scripts.turnoIngresosEgresos(user, turno)

        if turno.Felicidad >= Decimal(100):
            turno.Felicidad = Decimal(99.9)

        queryset = Turnos.objects.filter(User=user)
        serializer = TurnosSerializer(queryset, many=True)
        print("TE ENVIE",serializer.data)
        return JsonResponse(serializer.data, safe=False)

    @action(methods=['get', 'post'], detail=False)  #se necesita el usuario
    def felicidad(self, request):
        print("ENTROOOOO TURNOOOO INTERMEDIO")
        print("ME LLEGO = ",request.data)

        jsonFelicidad = request.data
        user = User.objects.filter(id = jsonFelicidad["UserID"]).first()

        afecta = Afecta_user.objects.filter(User=user)

        felicidad = []

        for afectaFelicidad in afecta:
            if str(afectaFelicidad.Afecta) == 'Felicidad':
                periodo = Periodo.objects.filter(Turnos=afectaFelicidad.TurnosEsperar).first()
                duracion = str(afectaFelicidad.Duracion)
                if afectaFelicidad.Duracion > 1000:
                    duracion = "infinito"
                felicidad.append({"Decripcion":afectaFelicidad.Descripcion, "Cantidad":afectaFelicidad.Cantidad, "Periodo":periodo.TipoPeriodo, "Duracion":duracion})
  
        return JsonResponse(felicidad, safe=False)


###################################################################

###################################################################

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = TipoPrestamo.objects.all()
    serializer_class = PrestamosSerializer


    @action(methods=['get', 'post'], detail=False)
    def catalogo(self, request):
        print("ENTROOOOO CATALOGO PRESTAMOS")
        print("ME LLEGO = ",request.data)
        queryset = TipoPrestamo.objects.all()
        serializer = PrestamosSerializer(queryset, many=True)
        print("TE ENVIE",serializer.data)
        return JsonResponse(serializer.data, safe=False)

    @action(methods=['put'], detail=False)
    def Realizar(self, request):
        print("ENTROOOOO RALIZAR PRESTAMO")
        print("ME LLEGO = ",request.data)
        jsonPrestamo = request.data

        minimoAprobatorio = jsonPrestamo["ValorTotal"] * .10

        if jsonPrestamo["Enganche"] < minimoAprobatorio:
            return JsonResponse({"mensaje": "El enganche no puede ser menor al 10 porciento del valor total"}, safe=False)

        if jsonPrestamo["Enganche"] >= jsonPrestamo["ValorTotal"]:
            return JsonResponse({"mensaje": "El enganche es mayor al prestamo pedido"}, safe=False)

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
            print("TE ENVIE",{"mensaje": "No cuentas con los ingresos necesarios para realizar este pedido"})
            return JsonResponse({"mensaje": "No cuentas con los ingresos necesarios para realizar este pedido"}, safe=False)

        prestamoUser = Prestamo(User=user, idPrestamo=tipoPrestamo, ValorTotal=jsonPrestamo["ValorTotal"], CantidadPrestada=cantidadPrestada, Enganche=jsonPrestamo["Enganche"], Frecuencia=4, Amortizacion=0, Interes=interesMensual, Mensualidad=pagoMensual, AbonoCapital=0, SaldoAbsoluto=cantidadPrestada )
        prestamoUser.save()

        #turno.DineroEfectivo = turno.DineroEfectivo + Decimal(cantidadPrestada)
        turno.DineroEfectivo = turno.DineroEfectivo - Decimal(jsonPrestamo["Enganche"])
        turno.save()
        print("TE ENVIE",{"mensaje":"Se a realizado el prestamo de forma exitosa"})
        return JsonResponse({"mensaje":"Se a realizado el prestamo de forma exitosa"}, safe=False)

    @action(methods=['put'], detail=False)
    def Amortizacion(self, request):
        print("ENTROOOOO AMORTIZACION")
        print("ME LLEGO = ",request.data)
        jsonPrestamo = request.data

        user = User.objects.filter(id = jsonPrestamo["UserID"]).first()
        turno = Turnos.objects.filter(User=user).first()
        prestamo = Prestamo.objects.filter(id = jsonPrestamo["PrestamoID"], User = user).first()
        
        if prestamo.SaldoAbsoluto < jsonPrestamo["Amortizacion"]:
            print("TE ENVIE",{"mensaje": "El saldo absoluto es menos que la amortización"})
            return JsonResponse({"mensaje": "El saldo absoluto es menos que la amortización"}, safe=False)
        
        #print("Dinero de turno = ", turno.DineroEfectivo)

        if turno.DineroEfectivo <= jsonPrestamo["Amortizacion"]:
            print("TE ENVIE",{"mensaje": "No tienes la cantidad requerida para esta accion"})
            return JsonResponse({"mensaje": "No tienes la cantidad requerida para esta accion"}, safe=False)

        if jsonPrestamo["Amortizacion"] <= 0:
            print("TE ENVIE",{"mensaje": "Cantidad no valida"})
            return JsonResponse({"mensaje": "Cantidad no valida"}, safe=False)

        prestamo.AbonoCapital = jsonPrestamo["Amortizacion"] + prestamo.AbonoCapital

        prestamo.SaldoAbsoluto = prestamo.SaldoAbsoluto - jsonPrestamo["Amortizacion"]

        if prestamo.SaldoAbsoluto < prestamo.Mensualidad:
            prestamo.Mensualidad = prestamo.SaldoAbsoluto

        prestamo.save()

        if prestamo.SaldoAbsoluto <= 0:
            prestamo.delete()
        
        turno.DineroEfectivo = turno.DineroEfectivo - Decimal(jsonPrestamo["Amortizacion"])
        turno.save()
        print("TE ENVIE",{"mensaje":"Se realizo la amoritizacion de forma correcta"},)
        return JsonResponse({"mensaje":"Se realizo la amoritizacion de forma correcta"}, safe=False)
    
    @action(methods=['get', 'post'], detail=False)
    def prestamosActuales(self, request):
        print("ENTROOOOO PRESTAMOS ACTUALES")
        print("ME LLEGO = ",request.data)
        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        actuales = Prestamo.objects.filter(User=user)

        prestamosActuales = []

        for prestamo in actuales:
            tipoPrestamo = TipoPrestamo.objects.filter(id = prestamo.idPrestamo.id).first()
            mesesRestantes = math.ceil(prestamo.SaldoAbsoluto/prestamo.Mensualidad)
            prestamosActuales.append({'PrestamoID':prestamo.id, 'TipoPrestamo':tipoPrestamo.TipoPrestamo, 'Mensualidad':prestamo.Mensualidad, "SaldoAbsoluto":prestamo.SaldoAbsoluto, "MesesRestantes":mesesRestantes})
        
        print("TE ENVIE ",prestamosActuales)
        return JsonResponse(prestamosActuales, safe=False)


###################################################################

###################################################################
class InversionViewSet(viewsets.ModelViewSet):
    queryset = TipoInversiones.objects.all()
    serializer_class = TipoInversionesSerializer

    @action(methods=['get', 'post'], detail=False)
    def catalogoDisponibles(self, request):
        print("ENTROOOOO CATALOGO DISPONIBLES")
        print("ME LLEGO = ",request.data)
        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        actuales = Inversion.objects.filter(User=user)
        catalogo = TipoInversiones.objects.all()

        for inversionActual in actuales:
            catalogo = catalogo.exclude(id=inversionActual.TipoInversion.id)

        queryset = catalogo
        serializer = TipoInversionesSerializer(queryset, many=True)
        print("TE ENVIE ",serializer.data)
        return JsonResponse(serializer.data, safe=False)

    @action(methods=['get', 'post'], detail=False)
    def inversionesActuales(self, request):
        print("ENTROOOOO INVERSIONES ACTUALES")
        print("ME LLEGO = ",request.data)
        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        actuales = Inversion.objects.filter(User=user)

        queryset = actuales
        serializer = InversionesSerializer(queryset, many=True)
        print("TE NEVIE = ",serializer.data)
        return JsonResponse(serializer.data, safe=False)
    
    @action(methods=['get', 'post'], detail=False)
    def inversionesPersonalesActuales(self, request):
        print("ENTROOOOO INVERSIONES PERSONALES")
        print("ME LLEGO = ",request.data)
        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()

        inversionesAfecta = Afecta_user.objects.filter(Afecta__startswith = 'Inversion', User = user.id)
        inversionPregunta = InversionPregunta.objects.filter(User = user.id)

        inversiones = []

        for afecta in inversionesAfecta:
            periodo = Periodo.objects.filter(Turnos=afecta.TurnosEsperar).first()
            inversiones.append({'id':afecta.id, 'TipoInversion': 'FlujoEfectivo', 'Cantidad':afecta.Cantidad, 'Periodo': periodo.TipoPeriodo})

        for inverPregunta in inversionPregunta:
            inversiones.append({'id':inverPregunta.id, 'TipoInversion':'GananciaCapital', 'Inicio':inverPregunta.SaldoInicial, 'Actual':inverPregunta.SaldoActual})

        print("TE ENVIE = ",inversiones)
        return JsonResponse(inversiones, safe=False)
    
    @action(methods=['post'], detail=False)
    def nueva(self, request):
        print("ENTROOOOO NUEVA INVERSION")
        print("ME LLEGO = ",request.data)
        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        turno = Turnos.objects.filter(User=user).first()
        compania = TipoInversiones.objects.filter(id=jsonInversion["InversionID"]).first()

        if turno.DineroEfectivo < Decimal(jsonInversion['Cantidad']):
            print("TE ENVIE = ",{"mensaje": "No cuentas con el dinero para realizar esta accion"})
            return JsonResponse({"mensaje": "No cuentas con el dinero para realizar esta accion"}, safe=False)

        rangoRendimiento = (compania.RangoRendimiento).split(" ")
        limite_inferior = float(rangoRendimiento[0])
        limite_superior = float(rangoRendimiento[2])
        tasaRendimiento = random.uniform(limite_inferior,limite_superior)
        nuvaInversion = Inversion(User=user,TipoInversion=compania,NombreInversion=compania.Inversion,TipoEmpresa=compania.TipoInversion,SaldoInicial=jsonInversion['Cantidad'],SaldoAportacion=jsonInversion['Cantidad'],EventoExterno=0,TasaRendimiento=tasaRendimiento,Aportacion=0,SaldoActual=jsonInversion['Cantidad'])
        nuvaInversion.save()

        turno.DineroEfectivo = turno.DineroEfectivo - Decimal(jsonInversion['Cantidad'])
        turno.save()

        print("TE ENVIE = ",{"mensaje":"Se realizo la nueva inversion de forma exitosa"})
        return JsonResponse({"mensaje":"Se realizo la nueva inversion de forma exitosa"}, safe=False)

    @action(methods=['put'], detail=False)
    def agregarDinero(self, request):
        print("ENTROOOOO AGREGAR DINERO")
        print("ME LLEGO = ",request.data)
        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        turno = Turnos.objects.filter(User=user).first()

        inversion = Inversion.objects.filter(id=jsonInversion["InversionID"]).first()
        
        if jsonInversion["Cantidad"] > turno.DineroEfectivo:
            print("TE ENVIE = ",{"mensaje":"No cuentas con la cantidad de dinero para realizar esta accion"})
            return JsonResponse({"mensaje":"No cuentas con la cantidad de dinero para realizar esta accion"}, safe=False)

        if jsonInversion["Cantidad"] <= 0:
            print("TE ENVIE = ",{"mensaje":"Cantidad no valida"})
            return JsonResponse({"mensaje":"Cantidad no valida"}, safe=False)

        inversion.SaldoAportacion = inversion.SaldoAportacion + jsonInversion["Cantidad"]
        inversion.SaldoActual = inversion.SaldoActual + jsonInversion["Cantidad"]
        inversion.save()

        turno.DineroEfectivo = turno.DineroEfectivo - Decimal(jsonInversion["InversionID"])
        turno.save()
        
        print("TE ENVIE = ",{"mensaje": "Se realizo la transaccion de forma correcta"})
        return JsonResponse({"mensaje": "Se realizo la transaccion de forma correcta"}, safe=False)

    @action(methods=['put'], detail=False)
    def retirarDinero(self, request):
        print("ENTROOOOO RETIRAR DINERO")
        print("ME LLEGO = ",request.data)
        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        turno = Turnos.objects.filter(User=user).first()
        inversion = Inversion.objects.filter(id=jsonInversion["InversionID"]).first()

        if jsonInversion["Cantidad"] >= inversion.SaldoActual:
            print("TE ENVIE = ",{"mensaje":"No cuentas con suficiente dinero para retirar esta cantidad"})
            return JsonResponse({"mensaje":"No cuentas con suficiente dinero para retirar esta cantidad"}, safe=False)

        if jsonInversion["Cantidad"] <= 0:
            print("TE ENVIE = ",{"mensaje":"Cantidad no valida"})
            return JsonResponse({"mensaje":"Cantidad no valida"}, safe=False)

        inversion.Aportacion = inversion.Aportacion + jsonInversion["Cantidad"]
        inversion.SaldoActual = inversion.SaldoActual - Decimal(jsonInversion["Cantidad"])
        inversion.save()

        turno.DineroEfectivo = turno.DineroEfectivo + Decimal(jsonInversion["Cantidad"])
        turno.save()
        
        print("TE ENVIE = ",{"mensaje": "La transaccion se realizo de forma correcta"})
        return JsonResponse({"mensaje": "La transaccion se realizo de forma correcta"}, safe=False)

    @action(methods=['put'], detail=False)
    def retirarAccion(self, request):
        print("ENTROOOOO RETIRAR ACCION")
        print("ME LLEGO = ",request.data)
        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        turno = Turnos.objects.filter(User=user).first()
        inversion = Inversion.objects.filter(id=jsonInversion["InversionID"]).first()

        turno.DineroEfectivo = turno.DineroEfectivo + inversion.SaldoActual
        inversion.delete()
        turno.save()
        
        print("TE ENVIE = ",{"mensaje": "Se retiro la accion de forma correcta"})
        return JsonResponse({"mensaje": "Se retiro la accion de forma correcta"}, safe=False)

    @action(methods=['put'], detail=False)
    def retirarInversionPersonal(self, request):
        print("ENTROOOOO RETIRAR INVERSION PERSONAL")
        print("ME LLEGO = ",request.data)
        jsonInversion = request.data
        user = User.objects.filter(id = jsonInversion['UserID']).first()
        turno = Turnos.objects.filter(User=user).first()
        inversion = InversionPregunta.objects.filter(id=jsonInversion["InversionID"]).first()

        turno.DineroEfectivo = turno.DineroEfectivo + inversion.SaldoActual
        inversion.delete()
        turno.save()
        
        print("TE ENVIE = ",{"mensaje": "Se retiro la accion de forma correcta"})
        return JsonResponse({"mensaje": "Se retiro la accion de forma correcta"}, safe=False)

###################################################################

###################################################################
class PortafolioViewSet(viewsets.ModelViewSet):

    @action(methods=['get', 'post'], detail=False)
    def financiero(self, request):
        print("ENTROOOOO PORTAFOLIO FINANCIERO")
        print("ME LLEGO = ",request.data)
        jsonPortafolio = request.data
        user = User.objects.filter(id = jsonPortafolio['UserID']).first()
        turno = Turnos.objects.filter(User=user).first()
        prestamos = Prestamo.objects.filter(User = user.id)
        inversiones = Inversion.objects.filter(User = user.id)
        ingresos = Afecta_user.objects.filter(Afecta = 'Ingresos', User = user.id)
        egresos = Afecta_user.objects.filter(Afecta = 'Egresos', User = user.id)
        inversionesAfecta = Afecta_user.objects.filter(Afecta__startswith = 'Inversion', User = user.id)
        inversionPregunta = InversionPregunta.objects.filter(User = user.id)

        portafolio = {'Egresos':[], 'Ingresos':[]}

        portafolio['Ingresos'].append({"Tipo":"Ingreso", "Nombre":"Sueldo","Cantidad":turno.Sueldo, "Periodo":"Mensual"})

        for prestamo in prestamos:
            nombrePrestamo = TipoPrestamo.objects.filter(idPrestamo = prestamo.idPrestamo.id).first()
            nombre = "Prestamo " + str(nombrePrestamo.TipoPrestamo)
            portafolio['Egresos'].append({"Tipo":"Egreso", "Nombre":nombre, "Cantidad":prestamo.Mensualidad, "Periodo":"Mensual"})

        for inversion in inversiones:
            compania = TipoInversiones.objects.filter(id=inversion.TipoInversion.id).first()
            portafolio['Ingresos'].append({"Tipo":"Ingreso", "Nombre":compania.Inversion, "Cantidad":inversion.SaldoActual, "Periodo":"Activo"})

        for ingreso in ingresos:
            periodo = Periodo.objects.filter(Turnos=ingreso.TurnosEsperar).first()
            portafolio['Ingresos'].append({"Tipo":"Ingreso", "Nombre":ingreso.Descripcion, "Cantidad":ingreso.Cantidad, "Periodo":periodo.TipoPeriodo})

        for egreso in egresos:
            periodo = Periodo.objects.filter(Turnos=egreso.TurnosEsperar).first()
            portafolio['Egresos'].append({"Tipo":"Egreso", "Nombre":egreso.Descripcion, "Cantidad":egreso.Cantidad, "Periodo":periodo.TipoPeriodo})

        for invercionAfe in inversionesAfecta:
            periodo = Periodo.objects.filter(Turnos=invercionAfe.TurnosEsperar).first()
            portafolio['Ingresos'].append({"Tipo":"Ingreso", "Nombre":invercionAfe.Descripcion, "Cantidad":invercionAfe.Cantidad, "Periodo":periodo.TipoPeriodo})
            
        for inversionPreg in inversionPregunta:
            tipoInversion = TipoPregunta.objects.filter(id=inversionPreg.TipoInversion.id).first()
            portafolio['Ingresos'].append({"Tipo":"Ingreso", "Nombre":tipoInversion.TipoPregunta, "Cantidad":inversionPreg.SaldoActual, "Periodo":"Activo"})
        
        print("TE ENVIE = ",portafolio)
        return JsonResponse(portafolio, safe=False)

    
###################################################################

###################################################################
class FinJuegoViewSet(viewsets.ModelViewSet):

    @action(methods=['put'], detail=False)
    def juego(self, request):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("ENTROOOOO FIN DEL JUEGO")
        print("ME LLEGO = ",request.data)
        jsonUser = request.data
        user = User.objects.filter(id = jsonUser['UserID']).first()

        scripts.borrarInfoUser(user)
        scripts.reiniciarUser(user)

        print("TE ENVIE = ",{})
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        return JsonResponse({"mensaje":"Fin del juego"}, safe=False)



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
    
