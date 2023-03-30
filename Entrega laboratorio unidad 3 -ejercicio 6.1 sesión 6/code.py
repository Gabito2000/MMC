# Ejercicios - Entrega 3
# Ejercicio 6.1: [individual]
# Problema: se idealiza una monta˜na como un cono inscrito en una regi´on
# cuadrada de lado 1 km. La base de la monta˜na es circular, con centro en
# (0.5, 0.5) y radio r = 0.4km, y la altura es H = 8km. La altura de cada
# punto (x, y) de la monta˜na est´a dada por la funci´on
# f(x, y) = H − H/r ×
# p
# (x − 0.5)2 + (y − 0.5)2, en la zona definida por el
# c´ırculo, y 0 fuera del c´ırculo. El volumen total de la monta˜na (en km
# c´ubicos) puede verse como la integral de la funci´on altura en la regi´on.
# • Parte a: escribir un programa para calcular el vol´umen por Monte Carlo.
# Realizar 106
# replicaciones y estimar el valor de ζ y el error cometido
# (con nivel de confianza 0.95), utilizando como criterio la aproximaci´on
# normal.
# • Parte b: en base al valor estimado en la parte a, calcular el n´umero de
# 20
# replicaciones necesario para obtener un error absoluto menor a 10−3
# (con nivel de confianza 0.95).
# • Parte c: realizar esa cantidad de replicaciones y estimar ζ y su intervalo
# de confianza.
# Comentario - en un s´olido regular como el del ejercicio, este volumen
# podr´ıa calcularse tambi´en anal´ıticamente. En el caso de una monta˜na real,
# la altura para cada punto no va a surgir de una f´ormula, sino que se debe
# usar informaci´on de altura procedente de mediciones reales, por ejemplo de
# informaci´on satelital

import random
import math
import scipy.stats as stats
import time

random.seed(1402)

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
        x_al = random.uniform(0, 1)
        y_al = random.uniform(0, 1)
        if j > 1:
            T = T + (1 - 1/j) * (funcion(x_al,y_al) - S/ (j-1))**2
        S = S + funcion(x_al,y_al)

    estimacion_integral = S / n
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