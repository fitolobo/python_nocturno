import pandas as pd  #csv-xlsm
import os            #directories
import time          #spend time


### LIMPIEZA
### DIRECTORIOS
path = os.getcwd()
directory_files = '/OneDrive-2022-01-29/'


### FUNCION DE RECOLECCION DE LOS XLSM #########################################
### CONTADOR DE ARCHIVOS###
count = 0
### NUEVOS NOMBRES PARA LAS COLUMNAS DE LOS XLSM ###############################
column_names = ["fecha","horas","cod","nombre"]
archivos = list()

start_time = time.time()

for subdir, dirs, files in os.walk(path+directory_files):
    for file in files:
        count += 1
        try:
            print(file)
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



#### CAPTURAR HORAS Y FILAS PARA SUMAR POSTERIORMENTE ##########################

i = 0
rangos_de_tiempo = list()
##### tener los tiempos ######
for dia in cristian.fecha:
    
    if not pd.isna(dia):
        print((dia,i))
        rangos_de_tiempo.append(i)
    i += 1
###############################


# partida
lim_inf = 0
lim_sup = 2

for i in range(len(rangos_de_tiempo)-1):

    # agarro el intervalo
    intervalo = rangos_de_tiempo[lim_inf:lim_sup]

    # me adelanto para la modificacion del intervalo en la siguiente iteracion
    lim_inf = i + 1
    lim_sup = i + 3
################################################################################
