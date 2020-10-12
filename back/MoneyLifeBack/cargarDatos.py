import numpy as np
import pandas as pd
import os
import pymysql
from pathlib import Path

def cargarBase(paginas):
    try:
        db = pymysql.connect("localhost","moneylifeuser","moneylifeuser#","MoneyDB")
        cursor = db.cursor()
    except pymysql.Error as e :
            print("could not close connection error pymysql %d: %s" %(e.args[0], e.args[1]))

    for key, pagina in paginas.items():
        print(pagina)
        print('\n')
        for index, row in pagina.iterrows():
            print('\n')
    
    cursor.close()

def main(archivobd):

    paginas = pd.read_excel(archivobd,sheet_name = None)
    cargarBase(paginas)

if __name__ == "__main__":
    folder = Path("Files/")
    archivobd =  folder / os.listdir('Files/')[0]
    print(archivobd)
    main(archivobd)
