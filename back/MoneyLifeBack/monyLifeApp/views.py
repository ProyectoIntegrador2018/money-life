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
import pandas as pd
import numpy as np
import random
import json
import re

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
        print("ENTROOOOO INICIOOOO TURNOOOO")
        jsonUser = request.data
        user = User.objects.filter(id = jsonUser['UserID']).first() 
        eventos = seleccionEvento(user)
        output = json.dumps(eventos)
        response = json.loads(output)
        print("Response = ",response)

        modifyEvento(user, response) #Modifica la frcuencia del evento que se utilizo
        eventoAfecta(user, response) #Crea los afecta del evento que se utilizo

        return JsonResponse(response, safe = False)

#Funciones que llaman los servicios de eventos
def modifyEvento(user, eventos):
    if eventos != None:
        for evento in eventos:
            if evento != {}:
                changefrecuencia = Evento_User.objects.get(User=user.id, Evento=evento['Evento_id'])
                Evento_User.objects.filter(User=user.id, Evento=evento['Evento_id']).update(Frecuencia=changefrecuencia.Frecuencia - 1)
    
def eventoAfecta(user, eventos):
    print("Eventos = ",eventos)
    if eventos != None:
        for evento in eventos:
            if evento != {}:
                afecta_evento = Evento_Afecta.objects.filter(Evento=evento['Evento_id'])
                for afecta in afecta_evento:
                    duracion = Periodo.objects.filter(TipoPeriodo=afecta.Periodo).first()
                    afecta_usuario = Afecta_user(User=user, Descripcion=evento["Descripcion"], Afecta=afecta.Afecta, TurnosEsperar=duracion.Turnos, TurnosRestante=duracion.Turnos, Cantidad=afecta.Cantidad, Duracion=afecta.Duracion)
                    afecta_usuario.save()

def verificarRequisitos(id, turno, flag_tipo):
    print('Requisitosfunc')
    if(flag_tipo == 'Pregunta'):
        requisitos = Preguntas_Requisitos.objects.filter(Preguntas_id = id)
    else:
        requisitos = Evento_Requisitos.objects.filter(Evento = id)
    if not requisitos:
        return True
    else:
        for requisito in requisitos:
            req = str(requisito.Requisito)
            cant = str(requisito.Cantidad)
            if (req == 'Felicidad'):
                if(cant[0] == '>'):
                    if(turno.Felicidad > int(cant.split('>')[1])):
                        pass
                    else:
                        return False
                elif(cant[0] == '<'):
                    if(turno.Felicidad < int(cant.split('<')[1])):
                        pass
                    else:
                        return False
                elif(cant.find('-') > 0):
                    if ((turno.Felicidad >= int(cant.split('-')[0])) and (turno.Felicidad <= int(cant.split('-')[1]))):
                        pass
                    else:
                        return False
                elif(cant[0] == '='):
                    if (turno.Felicidad == int(cant.split('=')[1]) ):
                        pass
                    else:
                        return False
                        
            elif (req == 'Ingresos'):
                if(cant[0] == '>'):
                    if(turno.Ingresos > int(cant.split('>')[1])):
                        pass
                    else:
                        return False
                elif(cant[0] == '<'):
                    if(turno.Ingresos < int(cant.split('<')[1])):
                        pass
                    else:
                        return False
                elif(cant[0] == '='):
                    if(turno.Ingresos < int(cant.split('=')[1])):
                        pass
                    else:
                        return False
                elif(cant.find('-') > 0):
                    if ((turno.Ingresos >= int(cant.split('-')[0])) and (turno.Ingresos <= int(cant.split('-')[1]))):
                        pass
                    else:
                        return False
                
            elif (req == 'NumeroTurnos'):
                if(cant[0] == '>'):
                    if(turno.NumeroTurnos > int(cant.split('>')[1])):
                        pass
                    else:
                        return False
                elif(cant[0] == '<'):
                    if(turno.NumeroTurnos < int(cant.split('<')[1])):
                        pass
                    else:
                        return False
                elif(cant[0] == '='):
                    if(turno.NumeroTurnos < int(cant.split('=')[1])):
                        pass
                    else:
                        return False
                elif(cant.find('-') > 0):
                    if ((turno.NumeroTurnos >= int(cant.split('-')[0])) and (turno.NumeroTurnos <= int(cant.split('-')[1]))):
                        pass
                    else:
                        return False
            elif (req == 'DineroEfectivo'):
                if(cant[0] == '>'):
                    if(turno.NumeroTurnos > int(cant.split('>')[1])):
                        pass
                    else:
                        return False
                elif(cant[0] == '<'):
                    if(turno.NumeroTurnos < int(cant.split('<')[1])):
                        pass
                    else:
                        return False
                elif(cant[0] == '='):
                    if(turno.NumeroTurnos < int(cant.split('=')[1])):
                        pass
                    else:
                        return False
                elif(cant.find('-') > 0):
                    if ((turno.NumeroTurnos >= int(cant.split('-')[0])) and (turno.NumeroTurnos <= int(cant.split('-')[1]))):
                        pass
                    else:
                        return False
            elif (req == 'Egresos'):
                if(cant[0] == '>'):
                    if(turno.Egresos > int(cant.split('>')[1])):
                        pass
                    else:
                        return False
                elif(cant[0] == '<'):
                    if(turno.Egresos < int(cant.split('<')[1])):
                        pass
                    else:
                        return False
                elif(cant[0] == '='):
                    if(turno.Egresos < int(cant.split('=')[1])):
                        pass
                    else:
                        return False
                elif(cant.find('-') > 0):
                    if ((turno.Egresos >= int(cant.split('-')[0])) and (turno.Egresos <= int(cant.split('-')[1]))):
                        pass
                    else:
                        return False
        return True

def getSeleccion(queryset, tipoEvento, eventos, turno):
    df = pd.DataFrame(list(queryset.values()))
    df['FrecuenciaAcumulada'] = df['Frecuencia'].cumsum()
    limite_inferior = df['FrecuenciaAcumulada'].min()
    limite_superior = df['FrecuenciaAcumulada'].max()
    seleccion = random.uniform(limite_inferior,limite_superior)
    for index, row in df.iterrows():
        if (row['FrecuenciaAcumulada'] >= seleccion):
            if(tipoEvento == 'Micro'):
                print("ENTRA")
                if(verificarRequisitos(row['Evento_id'], turno,'Evento')):
                    print("SALE")
                    desc = Evento.objects.get(id=row['Evento_id'])
                    desc = str(desc.Descripcion)
                    temp = row[['Evento_id']].to_dict()
                    temp['TipoEvento'] = 'Micro'
                    temp['Descripcion'] = desc
                    eventos.append(temp)
                    break
                else:
                    print("SALE")
                    pass
            else:
                temp = row[['Evento_id']].to_dict()
                desc = Evento.objects.get(id=row['Evento_id'])
                desc = str(desc.Descripcion)
                temp['TipoEvento'] = 'Macro'
                temp['Descripcion'] = desc
                eventos.append(temp)
                break


def seleccionEvento(user):
    turno = Turnos.objects.filter(User=user).first()
    eventos = []
    seleccion = 0
    eventosDisp = Evento_User.objects.values_list('Evento','Frecuencia','TipoEvento').exclude(Frecuencia=0)
    micro_id = TipoEvento.objects.get(TipoEvento = 'Micro').pk
    query_micro = eventosDisp.filter(TipoEvento=micro_id, User=user)
    if not query_micro:
        return eventos.append({})
    getSeleccion(query_micro, 'Micro', eventos, turno)
    seleccion = random.uniform(0,1)
    if(seleccion >= .7):
        macro_id = TipoEvento.objects.get(TipoEvento = 'Macro').pk
        query_macro = eventosDisp.filter(TipoEvento=macro_id, User=user)
        getSeleccion(query_macro, 'Macro', eventos, turno)
    else:
        eventos.append({})
    return eventos

###################################################################

###################################################################
class PreguntaViewSet(viewsets.ModelViewSet):

    @action(methods=['get'], detail=False)
    def getPreguntas(self, request):
        jsonUser = request.data
        user = User.objects.filter(id = jsonUser['UserID']).first()
        preguntas = seleccionPregunta(user)
        output = json.dumps(preguntas)
        response = json.loads(output)
        print(response)
        return JsonResponse(response, safe = False)

    @action(methods=['put'], detail=False)
    def afectaPreguntas(self, request):
        jsonPregunta = request.data
        
        user = User.objects.filter(id = jsonPregunta['UserID']).first()
        pregunta = Preguntas.objects.filter(id = jsonPregunta['PreguntaID']).first()

        #modifyPregunta(user, pregunta) #Modifica la frcuencia de la pregunta que se utilizo
        preguntaAfecta(user, pregunta)

        return JsonResponse({}, safe = False)

def modifyPregunta(user, pregunta):
    preguntaUser = Preguntas_User.objects.get(User=user.id, Pregunta=pregunta.id)
    Preguntas_User.objects.filter(User=user.id, Pregunta=pregunta.id).update(Frecuencia=preguntaUser.Frecuencia - 1)

def preguntaAfecta(user, pregunta):
    afecta_pregunta = Preguntas_Afecta.objects.filter(Preguntas=pregunta)
    tipoInversion = TipoPregunta.objects.filter(id=pregunta.TipoPreguntas.id).first()
    for afecta in afecta_pregunta:
        if tipoInversion.SaldoInversion != 'GananciaCapital':
            duracion = Periodo.objects.filter(TipoPeriodo=afecta.Periodo).first()
            afecta_usuario = Afecta_user(User=user, Descripcion=pregunta.Descripcion, Afecta=afecta.Afecta, TurnosEsperar=duracion.Turnos, TurnosRestante=duracion.Turnos, Cantidad=afecta.Cantidad, Duracion=afecta.Duracion)
            afecta_usuario.save()
        else:
            rangoRendimiento = (tipoInversion.TasaRendimiento).split(" ")
            limite_inferior = float(rangoRendimiento[0])
            limite_superior = float(rangoRendimiento[2])
            tasaRendimiento = random.uniform(limite_inferior,limite_superior)
            inversionPregunta = InversionPregunta(User=user, Descripcion=pregunta.Descripcion, TipoInversion=tipoInversion, SaldoInicial=afecta.Cantidad, InicialMasAportacion=afecta.Cantidad, EventoExterno=0, TazaRendimiento=tasaRendimiento, Aportacion=0, SaldoActual=afecta.Cantidad, SaldoInvercion= tipoInversion.SaldoInversion)
            inversionPregunta.save()

def getSeleccionPregunta(queryset, tipoEvento, preguntas, turno):
    df = pd.DataFrame(list(queryset.values()))
    for x in range(0,4,1):
        borrar = -10
        df['FrecuenciaAcumulada'] = df['Frecuencia'].cumsum()
        limite_inferior = df['FrecuenciaAcumulada'].min()
        limite_superior = df['FrecuenciaAcumulada'].max()
        seleccion = random.uniform(limite_inferior,limite_superior)
        for index, row in df.iterrows():
            if (row['FrecuenciaAcumulada'] >= seleccion):
                if(verificarRequisitos(row['Pregunta_id'], turno, 'Pregunta')):
                    desc = Preguntas.objects.get(id=row['Pregunta_id'])
                    desc = str(desc.Descripcion)
                    descTipo = TipoPregunta.objects.get(id=row['TipoPreguntas_id'])
                    descTipo = str(descTipo.TipoPregunta)
                    temp = row[['Pregunta_id']].to_dict()
                    temp['Descripcion'] = desc
                    temp['TipoEvento'] = descTipo
                    preguntas.append(temp)
                    borrar = index
                    print(row['Pregunta_id'])
                    print(row['TipoPreguntas_id'])
                    df.drop(borrar, inplace = True, errors = 'ignore' )
                    borrar = -10
                else:
                    pass
        

def seleccionPregunta(user):
    turno = Turnos.objects.filter(User=user).first()
    preguntas = []
    PreguntasDisp = Preguntas_User.objects.values_list('Pregunta','Frecuencia','TipoPreguntas').exclude(Frecuencia=0)
    inversion_id = TipoPregunta.objects.values_list('id',flat=True).filter(TipoPregunta__startswith = 'Inversion')
    diversion_id = TipoPregunta.objects.get(TipoPregunta = 'Diversion').pk
    bienes_id = TipoPregunta.objects.get(TipoPregunta = 'Bienes Personales').pk
    laboral_id = TipoPregunta.objects.get(TipoPregunta= 'Laboral').pk
    query_inversion = PreguntasDisp.filter(TipoPreguntas__in=inversion_id, User=user)
    query_diversion = PreguntasDisp.filter(TipoPreguntas=diversion_id,User=user)
    query_bienes = PreguntasDisp.filter(TipoPreguntas=bienes_id,User=user)
    query_laboral = PreguntasDisp.filter(TipoPreguntas=laboral_id,User=user)
    getSeleccionPregunta(query_inversion, 'Inversion', preguntas, turno)
    getSeleccionPregunta(query_diversion, 'Diversion', preguntas, turno)
    getSeleccionPregunta(query_bienes, 'Bienes Personales', preguntas, turno)
    getSeleccionPregunta(query_laboral, 'Laboral', preguntas, turno)
    return preguntas 


###################################################################

###################################################################
#LOGICA DE TURNOS

class TurnosViewSet(viewsets.ModelViewSet):
    queryset = Turnos.objects.all()
    serializer_class = TurnosSerializer

    #Este servicio se manda cada que inicie el turno
    @action(methods=['get'], detail=False)  #se necesita el usuario
    def inicio(self, request):
        jsonTurno = request.data
        user = User.objects.filter(id = jsonTurno["UserID"]).first()
        turno = Turnos.objects.filter(User=user).first()
        prestamos = Prestamo.objects.filter(User=user)
        inversiones = Inversion.objects.filter(User=user)
        inversionesPregunta = InversionPregunta.objects.filter(User = user)
        
        afectaTurnos(user, turno) #Llama a todos los afecta que esten relacionados con el usuario y los aplica
        prestamosTurnos(user, turno, prestamos) #Llama a todos los prestamos relacionados con este usuario para aplicar el gasto
        inversionesTurnos(user, turno, inversiones) #Llama a todas las inversiones relacionados con este usuario y aplica su flujo
        inversionesPreguntasTurnos(user, turno, inversionesPregunta)
        turnoIngresosEgresos(user, turno) #Calcula los ingresos y egresos mensuales de este turno

        queryset = Turnos.objects.filter(User=user)
        serializer = TurnosSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

#Se aplican todos los afectas relacionados con el usuario
def afectaTurnos(user, turno):
    
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
    if afecta == 'Felicidad':
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
    elif 'Inversion' in str(afecta):
        turno.DineroEfectivo = turno.DineroEfectivo + cantidad
    elif afecta == 'Ingresos':
        turno.DineroEfectivo = turno.DineroEfectivo + cantidad
    elif afecta == 'Egresos':
        turno.DineroEfectivo = turno.DineroEfectivo - cantidad

def turnoIngresosEgresos(user, turno):
   
    prestamos = Prestamo.objects.filter(User = user.id)
    inversiones = Inversion.objects.filter(User = user.id)
    ingresos = Afecta_user.objects.filter(Afecta = 'Ingresos', User = user.id)
    egresos = Afecta_user.objects.filter(Afecta = 'Egresos', User = user.id)
    inversionesAfecta = Afecta_user.objects.filter(Afecta__startswith = 'Inversion', User = user.id)
    inversionPregunta = InversionPregunta.objects.filter(User = user.id)

    turnoEgresos = 0
    turnoIngresos = 0

    for prestamo in prestamos:
        turnoEgresos = turnoEgresos + prestamo.Mensualidad

    #No es un ingreso por que no lo recibes mensualmente
    """
    for inversion in inversiones:
        turnoIngresos = turnoIngresos + inversion.SaldoActual
    """

    for ingreso in ingresos:
        portafolioCantidad = afectaMensual(ingreso)
        turnoIngresos = turnoIngresos + portafolioCantidad

    for egreso in egresos:
        portafolioCantidad = afectaMensual(egreso)
        turnoEgresos = turnoEgresos + portafolioCantidad

    for inversion in inversionesAfecta:
        portafolioCantidad = afectaMensual(inversion)
        turnoIngresos = turnoEgresos + portafolioCantidad

    #No es un ingreso por que no lo recibes mensualmente
    """
    for inversion in inversionPregunta:
        turnoIngresos = turnoIngresos + inversion.SaldoActual
    """

    turno.update(Ingresos=turnoIngresos, Egresos=turnoEgresos)

def afectaMensual(afecta):
    if afecta.TurnosEsperar > 4:
        numDividir = afecta.TurnosEsperar / 4
        afectaCantidad = afecta.Cantidad / Decimal(numDividir)
    elif afecta.TurnosEsperar == 2:
        afectaCantidad = afecta.Cantidad * 2
    elif afecta.TurnosEsperar == 1:
        afectaCantidad = afecta.Cantidad * 4
    else :
        afectaCantidad = afecta.Cantidad
    return afectaCantidad


def prestamosTurnos(user, turno, prestamos):

    for prestamo in prestamos:
        turno.DineroEfectivo = turno.DineroEfectivo - prestamo.Mensualidad
        tipoPrestamo = prestamo.idPrestamo
        
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

def inversionesTurnos(user, turno, inversiones):

    for inversion in inversiones:

        compania = TipoInversiones.objects.filter(id=inversion.TipoInversion.id).first()

        rangoRendimiento = (compania.RangoRendimiento).split(" ")
        limite_inferior = float(rangoRendimiento[0])
        limite_superior = float(rangoRendimiento[2])
        tasaRendimiento = random.uniform(limite_inferior,limite_superior)

        if inversion.EventoExterno != 0:
            inversion.SaldoActual = inversion.SaldoActual + (inversion.SaldoActual * Decimal(inversion.EventoExterno))
            inversion.EventoExterno == 0

        ###### ver el video del profe para entender bien como funciona ######
        inversion.TasaRendimiento = tasaRendimiento
        inversion.SaldoActual = inversion.SaldoActual + (inversion.SaldoActual * Decimal(inversion.TasaRendimiento))
        inversion.save()

def inversionesPreguntasTurnos(user, turno, inversionesPregunta):
    for inversion in inversiones:
        tipoInversion = TipoPregunta.objects.filter(id=inversion.TipoInversion.id).first()

        rangoRendimiento = (tipoInversion.TasaRendimiento).split(" ")
        limite_inferior = float(rangoRendimiento[0])
        limite_superior = float(rangoRendimiento[2])
        tasaRendimiento = random.uniform(limite_inferior,limite_superior)

        ###### ver el video del profe para entender bien como funciona ######
        inversion.TazaRendimiento = tasaRendimiento
        inversion.SaldoActual = inversion.SaldoActual + (inversion.SaldoActual * Decimal(inversion.TasaRendimiento))
        inversion.save()

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
class PortafolioViewSet(viewsets.ModelViewSet):

    @action(methods=['get'], detail=False)
    def financiero(self, request):
        jsonPortafolio = request.data
        user = User.objects.filter(id = jsonPortafolio['UserID']).first()

        prestamos = Prestamo.objects.filter(User = user.id)
        inversiones = Inversion.objects.filter(User = user.id)
        ingresos = Afecta_user.objects.filter(Afecta = 'Ingresos', User = user.id)
        egresos = Afecta_user.objects.filter(Afecta = 'Egresos', User = user.id)
        inversionesAfecta = Afecta_user.objects.filter(Afecta__startswith = 'Inversion', User = user.id)
        inversionPregunta = InversionPregunta.objects.filter(User = user.id)

        portafolio = []

        for prestamo in prestamos:
            nombrePrestamo = TipoPrestamo.objects.filter(idPrestamo = prestamo.idPrestamo).first()
            nombre = "Prestamo " + str(nombrePrestamo)
            portafolio.append({"Tipo":"Egreso", "Nombre":nombre, "Cantidad":prestamo.Mensualidad, "Periodo":"Mensual"})

        for inversion in inversiones:
            compania = TipoInversiones.objects.filter(id=inversion.TipoInversion.id).first()
            portafolio.append({"Tipo":"Ingreso", "Nombre":compania.Inversion, "Cantidad":inversion.SaldoActual, "Periodo":"Activo"})

        for ingreso in ingresos:
            periodo = Periodo.objects.filter(Turnos=ingreso.TurnosEsperar).first()
            portafolio.append({"Tipo":"Ingreso", "Nombre":ingreso.Descripcion, "Cantidad":ingreso.Cantidad, "Periodo":periodo.TipoPeriodo})

        for egreso in egresos:
            periodo = Periodo.objects.filter(Turnos=egreso.TurnosEsperar).first()
            portafolio.append({"Tipo":"Egreso", "Nombre":egreso.Descripcion, "Cantidad":egreso.Cantidad, "Periodo":periodo.TipoPeriodo})

        for invercionAfe in inversionesAfecta:
            periodo = Periodo.objects.filter(Turnos=invercionAfe.TurnosEsperar).first()
            portafolio.append({"Tipo":"Ingreso", "Nombre":invercionAfe.Descripcion, "Cantidad":invercionAfe.Cantidad, "Periodo":periodo.TipoPeriodo})
            
        for inversionPreg in inversionPregunta:
            tipoInversion = TipoPregunta.objects.filter(id=inversionPreg.TipoInversion.id).first()
            portafolio.append({"Tipo":"Ingreso", "Nombre":tipoInversion.TipoPregunta, "Cantidad":inversionPreg.SaldoActual, "Periodo":"Activo"})
        return JsonResponse(portafolio, safe=False)

    
###################################################################

###################################################################
class FinJuegoViewSet(viewsets.ModelViewSet):

    @action(methods=['put'], detail=False)
    def juego(self, request):
        jsonUser = request.data
        user = User.objects.filter(id = jsonUser['UserID']).first()

        user.delete()

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
    