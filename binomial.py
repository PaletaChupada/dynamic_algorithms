'''
Titulo: Calculo de coeficiente binomial
Descripcion: A partir de un numero solicitado al usuario y un coeficiente tambien solicitado al usuario, el programa realiza el calculo del coeficiente binomial a partir de estos numeros
Fecha: 16 de Mayo del 2022
Autor: Espinoza Bautista Daniel
'''

def binomialCheck(n, k, dp):
     
    # Si el valor esta en la tabla de busqueda se regresa el valor
    if dp[n][k] != -1:
        return dp[n][k]
 
    # Guardamos el valor en la tabla y posteriormente lo regresamos
    if k == 0:
        dp[n][k] = 1
        return dp[n][k]
     
    # Si se encuentra el numero regresamos el valor del numero y lo guardamos
    if k == n:
        dp[n][k] = 1
        return dp[n][k]
     
    # Guardamos el valor en la tabla de busqueda y realizamos el corrimiento del arreglo para realizar la busqueda
    dp[n][k] = (binomialCheck(n-1, k-1, dp) +
                binomialCheck(n-1, k, dp))
                 
    # Regresamos el arreglo de la tabla de busqueda
    return dp[n][k]

def binomial(n, k):
     
    # Creamos una tabla de busqueda temporal 
    dp = [ [ -1 for y in range(k + 1) ]
                for x in range(n + 1) ]
 
    # Realizamos el chequeo de la tabla para hacer la suma del coeficiente binomial
    return binomialCheck(n, k, dp)
 
# Solicitamos al usuario el numero al que calcularemos el coeficiente
n = int(input("Dame el valor del numero a calcular su coeficiente: "))

# Solicitamos al usuario el coeficiente para calcularle al numero
k = int(input("Dame el valor del coeficiente: "))
print("\n")
 
# Realizamos el calculo del coeficiente
print("Valor del coeficiente binomial de "+str(n)+"\n"+"Con coeficiente " +str(k)+"\n"+"Es: ",binomial(n, k))
