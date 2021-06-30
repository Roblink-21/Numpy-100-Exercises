import numpy as np

#Ejercicio 1
#Funcion  para la operacion
def operacion(arra1,k):
    result = np.add.reduceat(np.add.reduceat(arra1, np.arange(0, arra1.shape[0], k), axis=0),
                             np.arange(0, arra1.shape[1], k), axis=1)
    print (result)#Imprimimos el resultado

arreglo1 = np.ones((16,16))#creamos un arreglo llenos de uno

k = 4
print("Arreglo:")
print(arreglo1)#Imprimir arrreglo generado

print("\nBlocke-sum (4x4):")

operacion(arreglo1,k)

print("***************************")

#Ejercicio 2
#¿Cómo calcular promedios usando una ventana deslizante sobre una matriz?

n =3
def moving_average(a, n) :
    test = np.cumsum(a, dtype=float)
    test[n:] = test[n:] - test[:-n]
    return test[n - 1:] / n

print(moving_average(np.arange(20),n))

print("********************************")


#Ejercicio 3
#Considere un vector dado, ¿cómo agregar 1 a cada elemento indexado por un segundo
# vector (tenga cuidado con los índices repetidos)?
matriz1= np.ones(10)
print(matriz1)
matriz2 = np.random.randint(0,len(matriz1),20)
print(matriz2)
matriz1 += np.bincount(matriz2, minlength=len(matriz1))
print(matriz1)