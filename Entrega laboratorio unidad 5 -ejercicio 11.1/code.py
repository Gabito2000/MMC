# Entrega 6
# Ejercicio 11.1: (individual)
# Para generar un punto aleatorio (X1, X2) en un c´ırculo de centro (0, 0) y
# radio 1, es posible hacerlo de la forma siguiente (derivaci´on disponible en
# las p´aginas 234 y 235 del libro de referencia del curso, “Monte Carlo:
# concepts, algorithms and applications”, Fishman 1996):
# • se genera un valor aleatorio r, de distribuci´on Fr(x) = x
# 2 para
# 0 ≤ x ≤ 1, y 0 para cualquier otro x;
# • se generan dos v.a. independientes Z1 y Z2 de distribuci´on normal
# (0, 1);
# • se calcula X1 = rZ1/
# p
# (Z
# 2
# 1 + Z
# 2
# 2
# ) y X2 = rZ2/
# p
# (Z
# 2
# 1 + Z
# 2
# 2
# ).
# Utilizar esta propiedad para volver a resolver el Ejercicio 6.1 parte a, pero
# 20
# generando ´unicamente valores de puntos dentro del c´ırculo de base de la
# monta˜na:
# Problema: se idealiza una monta˜na como un cono inscrito en una regi´on
# cuadrada de lado 1 km. La base de la monta˜na es circular, con centro en
# (0.5, 0.5) y radio r = 0.4km, y la altura es H = 8km. La altura de cada
# punto (x, y) de la monta˜na est´a dada por la funci´on
# f(x, y) = H − H/r ×
# p
# (x − 0.5)2 + (y − 0.5)2, en la zona definida por el
# c´ırculo, y 0 fuera del c´ırculo. El volumen total de la monta˜na (en km
# c´ubicos) puede verse como la integral de la funci´on altura en la regi´on.
# Parte a: escribir un programa para calcular el vol´umen por Monte Carlo.
# Realizar 106
# replicaciones y estimar el valor de ζ y el error cometido (con
# nivel de confianza 0.95), utilizando como criterio la aproximaci´on normal.
# Comparar la precisi´on obtenida con la alcanzada en el ejercicio 6.1.
# Sugerencia: tener en cuenta que al estar generando puntos dentro del
# c´ırculo, estamos calculando una integral de Lebesgue-Stieltjes, por lo que
# es necesario ajustar el integrando de manera que quede expl´ıcita la integral
# 21
# en la forma R
# k(z)dF(z), con z un vector. En particular, por ser un sorteo
# uniforme dentro del c´ırculo, la densidad de probabilidad en el c´ırculo es
# 1/(´area del c´ırculo), y 0 afuera del mismo.
# Fecha entrega: Ver cronograma del curso.

# Teorema 1. Sea F(z), a ≤ z ≤ b una funci´on de distribuci´on, y su
# inversa F
# −1 definida por
# F^−1
# (u) = inf{z ∈ [a, b] : F(z) ≥ u, 0 ≤ u ≤ 1}.
# Sea U una variable aleatoria de distribuci´on uniforme U(0, 1). Entonces
# Z = F^−1
# (U) es una variable aleatoria de distribuci´on F.



import random
import math
import scipy.stats as stats
import time
import numpy as np


random.seed(1402)


# Función de distribución
def F(x):
    return x**2

# Inversa de la función de distribución
def invF(u):
    # a, b = 0, 1
    # z = np.linspace(a, b, 1000)
    # Fz = F(z)
    # idx = np.where(Fz >= u)[0][0]
    # return z[idx]
    return np.sqrt(u) # en nuestro caso es facil de notar que la inversa es la raiz cuadrada

# Generación de puntos aleatorios dentro del círculo
def generar_puntos(n):
    puntos = []
    for i in range(n):
        r = invF(random.uniform(0, 1)) # Generar r con distribución Fr(x) = x^2

        z1 = random.gauss(0, 1)  # Generar z1 y z2 con distribución normal
        z2 = random.normalvariate(0, 1)
        x1 = r*z1/np.sqrt(np.power(z1, 2) + np.power(z2, 2))  # Calcular x1 y x2
        x2 = r*z2/np.sqrt(np.power(z1, 2) + np.power(z2, 2))

        # reducir el radio a 0.4 y centrar el circulo en (0.5, 0.5)
        x1 = 0.4*x1 + 0.5
        x2 = 0.4*x2 + 0.5
        
        #convert to float
        x1 = float(x1)
        x2 = float(x2)
        puntos.append((x1, x2))  # Ajustar los puntos al círculo
    return puntos

#plot a graph of the points
def plot_graph(n):
    import matplotlib.pyplot as plt
    puntos = generar_puntos(n)
    x = [p[0] for p in puntos]
    y = [p[1] for p in puntos]
    plt.scatter(x, y)
    plt.show()
    


# plot_graph(1000)
# plot_graph(10000)
# plot_graph(100000)


print_tables = False

def  Calculo_intervalo_de_confianza(delta, estimado, n, varianza):
    CI_i = estimado - stats.norm.ppf(1 - delta/2) * math.sqrt(varianza/n)
    CI_f = estimado + stats.norm.ppf(1 - delta/2) * math.sqrt(varianza/n)
    return [CI_i, CI_f]


def IntegracionMonteCarlo(funcion, n, nivel_confianza):
    tiempo_inicial = time.time()
    S = 0
    T = 0
    for j in range(1, n+1):
        x_al, y_al = generar_puntos(1)[0]
        if j > 1:
            T = T + (1 - 1/j) * (funcion(x_al,y_al) - (S / (j-1)))**2
        S = S + funcion(x_al,y_al)
    estimacion_integral = (S / n) * (0.4**2 * math.pi) # multiplicamos por el area del circulo
    estimacion_varianza = T / (n - 1)
    estimacion_varianza_integral = estimacion_varianza / n
    
    intervalo_confianza = Calculo_intervalo_de_confianza(1 - nivel_confianza, estimacion_integral, n, estimacion_varianza)
    return estimacion_integral, estimacion_varianza_integral, intervalo_confianza , estimacion_varianza, time.time() - tiempo_inicial

def f(x, y):
    # Si se sale del círculo, la altura es 0
    if  ((x-0.5)**2 + (y-0.5)**2 )> (0.4)**2:
        return 0
    return 8 - (8/0.4 * math.sqrt((x - 0.5)**2 + (y - 0.5)**2))
    


def generate_html_table(estimacion_integral, estimacion_varianza_integral, intervalo_confianza, estimacion_varianza, tiempo_ejecucion):
    tabla_html = "<table><tr><th>Estimación</th><th>Varianza del estimador</th><th>Variaza de la integral</th><th>Intervalo de confianza</th><th>Tiempo de ejecución</th> </tr>"
    tabla_html += "<tr><td>" + str(estimacion_integral) + "</td><td>" + str(estimacion_varianza) + "</td><td>" + str(estimacion_varianza_integral) + "</td><td>" + str(intervalo_confianza) + "</td><td>" + str(tiempo_ejecucion) + "</td></tr>"
    tabla_html += "</table>"
    return tabla_html

# Parte a
n = 10**6
nivel_confianza = 0.95

estimacion_integral, estimacion_varianza_integral, intervalo_confianza, estimacion_varianza, tiempo_ejecucion = IntegracionMonteCarlo(f, n, nivel_confianza)

print("Parte a")
print("Estimación integral: ", estimacion_integral)
print("Estimación varianza: ", estimacion_varianza)
print("Estimación varianza integral: ", estimacion_varianza_integral)
print("Intervalo de confianza: ", intervalo_confianza)
print("Tiempo de ejecución: ", tiempo_ejecucion)

if print_tables:
    print(generate_html_table(estimacion_integral, estimacion_varianza_integral, intervalo_confianza, estimacion_varianza, tiempo_ejecucion))

# Parte b
def nN(epsilon, delta, estimacion_varianza):
    return math.ceil((stats.norm.ppf(1 - delta/2))**2 * (estimacion_varianza) / epsilon**2)

error = 10**(-3)
nivel_confianza = 0.95
delta = 1 - nivel_confianza
n = nN(error, delta, estimacion_varianza)

print("Parte b")
print("Número de muestras: ", n)

# Parte c
nivel_confianza = 0.95
estimacion_integral, estimacion_varianza_integral, intervalo_confianza, estimacion_varianza, tiempo_ejecucion = IntegracionMonteCarlo(f, n, nivel_confianza)
print("Parte c")
print("Estimación integral: ", estimacion_integral)
print("Estimación varianza: ", estimacion_varianza)
print("Estimación varianza integral: ", estimacion_varianza_integral)
print("Intervalo de confianza: ", intervalo_confianza)
print("Tiempo de ejecución: ", tiempo_ejecucion)

if print_tables:
    print(generate_html_table(estimacion_integral, estimacion_varianza_integral, intervalo_confianza, estimacion_varianza, tiempo_ejecucion))