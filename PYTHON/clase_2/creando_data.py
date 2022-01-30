### Leyendo data y creando data desde un excel (.csv, .tsv)
import pandas as pd  #llamar a la librería (que tiene un monton de funciones para leer, escribir y alterar .csv y otras extensiones)


# crear un  csv a mano!
nombre = ["Cristian","Fito","Paula"]
edad = [" ", "32", "31"]
comuna = ["Independencia","Maipú","huechuraba"]

dict = {"Nombres": nombre , "Edades": edad,
        "Comuna": comuna}

#########################
#Nombres    Edades   Comuna
#Cristian   "   "    ...
#Fito         32     ...
#Paula        31     ...
#########################


# aqui le damos una estructura "general"
df = pd.DataFrame(dict)    #desde pandas llama la funcion DataFrame y aplicala al diccionario dict

# que despues permite transformar a .csv u otros.
df.to_csv('ejemplo.csv')


### Leyendo

leyendo = pd.read_csv('ejemplo.csv')
print(leyendo)
