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
        eventos = seleccionEvento()
        output = json.dumps(eventos)
        response = json.loads(output)
        print(response)
        return JsonResponse(response, safe = False)

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

def verificarRequisitos(id):
    print('eventosRequisitosfunc')
    user = User.objects.filter(id = 2).first() #Esto son pruebas con el usuario
    turno = Turnos.objects.filter(User=user).first()
    requisitos = Evento_Requisitos.objects.filter(Evento = id)
    if not requisitos:
        return True
    else:
        for requisito in requisitos:
            req = str(requisito.Requisito)
            cant = str(requisito.Cantidad)
            event = str(requisito.Evento)
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
                elif(cant.find('-') > 0):
                    if ((turno.Egresos >= int(cant.split('-')[0])) and (turno.Egresos <= int(cant.split('-')[1]))):
                        pass
                    else:
                        return False
        return True

def getSeleccion(queryset, tipoEvento, eventos):
    df = pd.DataFrame(list(queryset.values()))
    df['FrecuenciaAcumulada'] = df['Frecuencia'].cumsum()
    limite_inferior = df['FrecuenciaAcumulada'].min()
    limite_superior = df['FrecuenciaAcumulada'].max()
    seleccion = random.uniform(limite_inferior,limite_superior)
    for index, row in df.iterrows():
        if (row['FrecuenciaAcumulada'] >= seleccion):
            if(tipoEvento == 'Micro'):
                if(verificarRequisitos(row['id'])):
                    temp = row[['id','Descripcion']].to_dict()
                    temp['TipoEvento'] = 'Micro'
                    eventos.append(temp)
                    break
                else:
                    pass
            else:
                temp = row[['id','Descripcion']].to_dict()
                temp['TipoEvento'] = 'Macro'
                eventos.append(temp)
                break

def seleccionEvento():
    micro_id = TipoEvento.objects.get(TipoEvento = 'Micro').pk        
    eventos = []
    query_micro = Evento.objects.filter(TipoEvento=micro_id)
    seleccion = 0
    getSeleccion(query_micro, 'Micro', eventos)
    seleccion = random.uniform(0,1)
    if(seleccion >= .7):
        macro_id = TipoEvento.objects.get(TipoEvento = 'Macro').pk
        query_macro = Evento.objects.filter(TipoEvento=macro_id)
        getSeleccion(query_macro, 'Macro', eventos)
    else:
        eventos.append({}) 
    
    return eventos

###################################################################

###################################################################
#LOGICA DE TURNOS

class TurnosViewSet(viewsets.ModelViewSet):
    queryset = Turnos.objects.all()
    serializer_class = TurnosSerializer

    #Este servicio se manda cada que inicie el turno
    @action(methods=['get', 'put'], detail=False)  #se necesita el usuario
    def inicio(self, request):

        afectaTurnos() #Llama a todos los afecta que esten relacionados con el cliente y los aplica

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
    