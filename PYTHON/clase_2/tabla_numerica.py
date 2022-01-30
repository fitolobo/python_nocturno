import pandas as pd  #dataframes: csv, tsv
import numpy as np   #libreria de algebra lineal y matematicas

# los valores que queremos operar
lista1 = np.random.rand(100)
lista2 = np.random.rand(100) + 10

# creamos un espacio vacio
espacio = list()

# creamos un iterador/Contador
for i in range(100):
    # aplicamos una formula consecutivamente a los elementos de las listas
    resultado = (lista1[i]*lista2[i])/12
    # guardamos la info en el espacio vacio
    espacio.append(resultado)

# crear el data frame: primero asociar columnas a listas
dict = {"lista1": lista1 , "lista2": lista2,
        "resultados": espacio}

# crear la estructura
df = pd.DataFrame(dict)

df.to_csv('ejemplo_2.csv',index = False)
