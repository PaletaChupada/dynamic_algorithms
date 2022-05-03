'''
Titulo: Caminos minimos
Descripcion: A partir de una matriz que se interpreta como nodos de una red, se solicita al usuario que nos indique el nodo inicial y el final y el programa se encarga de encontrar la ruta con los costos minimos dentro de toda la matriz
Fecha: 16 de Mayo del 2022
Autor: Espinoza Bautista Daniel
'''

# Tamaño de la matrix
R = 3
C = 3
 
# Definicion de la funcion de caminos
def camino(cost, m, n):
 
    # Inicializamos la matriz con el tamaño especificado anteriormente
    tc = [[0 for x in range(C)] for x in range(R)]
 
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
 
# Driver program to test above functions
cost = [[1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]]
print(camino(cost, 2, 2))

print("mina")
