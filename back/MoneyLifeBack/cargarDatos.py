import numpy as np
import pandas as pd
import os
import pymysql
from pathlib import Path

insert_afecta = "INSERT INTO afecta (`Tipo_Afecta`) VALUES(%s)"
insert_requisito = "INSERT INTO requisito (`Tipo_Requisito`) VALUES (%s)"
insert_periodo = "INSERT INTO periodo (`Tipo_Periodo`,`Turnos`) VALUES(%s,%s)"
insert_tipo_evento = "INSERT INTO tipo_evento (`Tipo_Evento`) VALUES (%s)"
insert_evento = "INSERT INTO tipo_evento (`Tipo_Evento`) VALUES (%s)"
insert_evento_afecta =
insert_evento_requisito =
insert_tipo_pregunta =
insert_pregunta =
insert_pregunta_afecta = 
insert_requisito =
insert_prestamo
insert_prestamo_afecta =
insert_acciones_cetes = 

def cargarBase(paginas):
    
    try:
        db = pymysql.connect("localhost","moneylifeuser","moneylifeuser#","MoneyDB")
        cursor = db.cursor()
    except pymysql.Error as e :
            print("could not create connection, error pymysql %d: %s" %(e.args[0], e.args[1]))

    for key, pagina in paginas.items():
        print(key)
        columnas = list(pagina.columns)
        query = "INSERT INTO %s () "

        print('\n')
        for index, row in pagina.iterrows():
            print('\n')
    
    cursor.close()

def cargarExcel():
    key_primera_pagina = 'General'
    try:
        folder = Path("Files/")
        archivobd =  folder / os.listdir('Files/')[0]
        #print(archivobd)
        paginas = pd.read_excel(archivobd,sheet_name = None)
        paginas.pop(key_primera_pagina)
        #print(paginas.keys())
        return paginas
    except:
        print('error al leer el archivo')
    

def main():
    paginas = cargarExcel()
    cargarBase(paginas) 


if __name__ == '__main__':
    main()


