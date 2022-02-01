import pandas as pd  #csv-xlsm
import os            #directories
import time          #spend time
from collections import Counter  #magia de sumar diccionarios!
from utils import preprocesamiento,periodos_tiempo,suma_horas_por_dia,suma_horas_por_dia,reset_codigos,magia
### LIMPIEZA
### DIRECTORIOS
path = os.getcwd()
directory_files = '/OneDrive-2022-01-29/'
################################################################################
################################################################################
################################################################################
################################################################################
################################################################################
### Pipeline
'''
    # NOTE: no olvidar agregar a cada uno de estos archivos el nombre o codigo
    del trabajador.
'''
PATH="codigos.csv"
codigos = pd.read_csv(PATH, index_col = False)
archivos,ID = preprocesamiento(path,directory_files)
L = len(archivos)

horas_mes_de_los_trabajadores = list()
horas_dia_de_los_trabajadores = list()


for i in range(L):

    ### Probando para un solo archivo!
    print("Excel: ")
    print(ID[i])
    print()

    archivo_i = archivos[i] #esto tiene que estar dentro de un loop que recorra los archivos
    rangos_de_tiempo = periodos_tiempo(archivo_i)
    horas_dia = suma_horas_por_dia(rangos_de_tiempo,archivo_i,codigos) # es una lista de diccionarios
    horas_mes =  magia(horas_dia)
    horas_mes_de_los_trabajadores.append(horas_mes)            # es una lista de diccionarios
    horas_dia_de_los_trabajadores.append(horas_dia)

# todos los trabajadores juntos!
horas_mes_total = magia(horas_mes_de_los_trabajadores)
################################################################################
