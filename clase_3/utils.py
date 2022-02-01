import pandas as pd  #csv-xlsm
import os            #directories
import time          #spend time
from collections import Counter  #magia de sumar diccionarios!
### FUNCION DE RECOLECCION DE LOS XLSM #########################################
### CONTADOR DE ARCHIVOS###
def preprocesamiento(path,directory_files):
    '''
        Elije del excel las filas y columnas de fecha, hora, codigo y nombre.
        Este proceso lo hace para todos los excel en un directorio.
        Obs: Todos deben tener el mismo formato.

        path: directorio principal (pwd)
        directory_files: directorio específico donde se encuentran los excel.

    '''
    count = 0
    ### NUEVOS NOMBRES PARA LAS COLUMNAS DE LOS XLSM ###############################
    column_names = ["fecha","horas","cod","nombre"]
    archivos = list()
    ID = list()
    start_time = time.time()

    for subdir, dirs, files in os.walk(path+directory_files):
        for file in files:
            count += 1
            try:
                print(file)
                ID.append(file)
                df = pd.read_excel(path+directory_files+file, index_col = False, sheet_name = None)
                tabla = df['HH'].iloc[10:149,1:5]
                tabla.columns = column_names

                archivos.append(tabla)

        ## If the file is not valid, skip it
            except ValueError:
                continue

            print("Total Number of XLSM Files")
            print(count)
            print("--- Data loaded. Loading time: %s seconds ---" % (time.time() - start_time))
    return archivos, ID


#### CAPTURAR HORAS Y FILAS PARA SUMAR POSTERIORMENTE ##########################
def periodos_tiempo(archivo_i):
    '''
        Almacena las filas donde se encuentran anotadas las horas de trabajo.
    '''
    i = 0
    rangos_de_tiempo = list()
    ##### tener los tiempos ######
    for dia in archivo_i.fecha:

        if not pd.isna(dia):
            rangos_de_tiempo.append(i)
        i += 1
    ###############################

    ultimo_valor = len(archivo_i.fecha) - rangos_de_tiempo[-1]
    rangos_de_tiempo.append(ultimo_valor)
    return rangos_de_tiempo

def suma_horas_por_dia(rangos_de_tiempo,archivo_i,codigos):
    '''
        Suma las horas trabajadas por dia y almacena la información en un diccionario
        donde la llave es el código de obra y los valores la suma de las horas trabajadas.
    '''
    # partida
    lim_inf = 0
    lim_sup = 2

    #dict_cod = {}

    horas_dia = []

    for i in range(len(rangos_de_tiempo)-1):

        # agarro el intervalo
        intervalo = rangos_de_tiempo[lim_inf:lim_sup]
        # me adelanto para la modificacion del intervalo en la siguiente iteracion
        lim_inf = i + 1
        lim_sup = i + 3

        dict_cod = reset_codigos(codigos)

        for j in range(intervalo[0],intervalo[1]):

            if not math.isnan(archivo_i.cod.iloc[j]):
                dict_cod[str(archivo_i.cod.iloc[j])] =+ archivo_i.horas.iloc[j] + dict_cod[str(archivo_i.cod.iloc[j])]

        horas_dia.append({x:y for x,y in dict_cod.items() if y!=0})

    return horas_dia
################################################################################
def reset_codigos(codigos):
    '''
        Resetea los valores del diccionario de codigos a cero.
    '''
    # reset del diccionario
    dict_cod = {}

    for i in range(1,len(codigos.codigos)):
        dict_cod[str(codigos.codigos[i])] = 0

    dict_cod["9020003"] = 0
    dict_cod["1021065"] = 0
    dict_cod["1021019"] = 0
    dict_cod["2021035"] = 0
    dict_cod["9020001"] = 0
    dict_cod["5021012"] = 0
    dict_cod["1021063"] = 0
    dict_cod["9020004"] = 0
    dict_cod["6315"] = 0
    dict_cod["1021076"] = 0
    dict_cod["6316"] = 0
    dict_cod["9345"] = 0
    return dict_cod

################################################################################
def magia(horas):
    aux = Counter(horas[0])
    for i in range(1,len(horas)):
        aux = aux + Counter(horas[i])
    return aux
