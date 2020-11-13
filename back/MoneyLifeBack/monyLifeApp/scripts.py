import pandas as pd
import numpy as np
from .models import *
import random

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
    df = df.sample(frac=1).reset_index(drop=True)
    for index, row in df.iterrows():
        if ((row['FrecuenciaAcumulada'] >= seleccion) and (verificarRequisitos(row['Evento_id'], turno,'Evento'))):
                desc = Evento.objects.get(id=row['Evento_id'])
                desc = str(desc.Descripcion)
                temp = row[['Evento_id']].to_dict()
                temp['Descripcion'] = desc
                if(tipoEvento == 'Micro'):
                        temp['TipoEvento'] = 'Micro'
                        eventos.append(temp)
                        break
                else:
                    temp['TipoEvento'] = 'Macro'
                    eventos.append(temp)
                    break
        else:
            pass



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
    df['FrecuenciaAcumulada'] = df['Frecuencia'].cumsum()
    limite_inferior = df['FrecuenciaAcumulada'].min()
    limite_superior = df['FrecuenciaAcumulada'].max()
    df = df.sample(frac=1).reset_index(drop=True)
    print(df)
    for x in range(0,4,1):
        borrar = -10
        seleccion = random.uniform(limite_inferior,limite_superior)
        for index, row in df.iterrows():
            if ((row['FrecuenciaAcumulada'] >= seleccion) and (verificarRequisitos(row['Pregunta_id'], turno, 'Pregunta'))):
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
                break
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