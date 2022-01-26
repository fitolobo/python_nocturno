

### Listas, Diccionarios y Vectores (Matrices)

          # 0   1   2
Lista_1 = ['a','b','c']

Lista_2 = [1,2,3]

Lista_3 = Lista_1 + Lista_2   # concatenar


Lista_4 = [Lista_1, Lista_2, Lista_3]

#print(Lista_3)
#print(Lista_1[1])
#print()
#print(Lista_1[1:3]) # llama desde la posicion 0
                 # hasta el final

print(Lista_4)
print(len(Lista_4[2])) # len() ¿Cual es el tamaño?



### Diccionarios
          #key #output
dict_1 = {"Nombre": 'Rodolfo', "Edad":14}
print(dict_1['Nombre'])


### vectores y matrices
import numpy   # genera vectores y todas sus operaciones

x = numpy.asarray([1,2,3])
y = numpy.asarray([-1,0,1])


M = numpy.ones((5,5))

matriz_a_mano= numpy.asarray([[1,2,3],[4,5,6],[7,8,9]])

print(x+y)
print(numpy.dot(x,y))
print(M)
print(matriz_a_mano)
print(matriz_a_mano*2)
