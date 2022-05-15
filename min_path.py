'''
Titulo: Caminos minimos
Descripcion: A partir de una matriz que se interpreta como nodos de una red, se solicita al usuario que nos indique el nodo inicial y el final y el programa se encarga de encontrar la ruta con los costos minimos dentro de toda la matriz
Fecha: 16 de Mayo del 2022
Autor: Espinoza Bautista Daniel
'''
# Importamos las librerias
import random

# Definicion de la funcion de caminos
def camino(cost, m, n, tam):
 
    # Inicializamos la matriz con el tamaño especificado anteriormente
    tc = [[0 for x in range(tam)] for x in range(tam)]
 
    # Anexamos a la posicion 0 el costo del camino 0
    tc[0][0] = cost[0][0]
 
    # Inicializamos la primer columna con el arreglo de los costos
    for i in range(1, m+1):
        tc[i][0] = tc[i-1][0] + cost[i][0]
 
    # Inizializamos la primer fila con los costos de la matriz tc
    for j in range(1, n+1):
        tc[0][j] = tc[0][j-1] + cost[0][j]
 
    # Construimos el resto del arreglo y calculamos el camino minimo a partir de los valores del nodo de inicio y nodo del fin
    for i in range(1, m+1):
        for j in range(1, n+1):
            tc[i][j] = min(tc[i-1][j-1], tc[i-1][j], tc[i][j-1]) + cost[i][j]
 
    # Retornamos la matriz con todos los costos ya hechos
    return tc[m][n]

# Definimos el valor del tamaño de la matriz
tam = 3

# Inicializamos la matriz con el tamaño especificado anteriormente
cost = [[0 for x in range(tam)] for x in range(tam)] 

# Valores de la matriz generados aleatoriamente entre 1 y 10
for i in range(len(cost)):
    for j in range(len(cost[i])):
        cost[i][j] = random.randint(1,10)

print("\nMatriz: ",cost)

print("\nCamino minimo: ",camino(cost, 2, 2, tam))
