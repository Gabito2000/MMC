# Ejercicio 14.1 (grupal): Partiendo de uno de los c´odigos elaborados para
# resolver el ejercicio 6.2, utilizar el m´etodo de muestreo estratificado para
# calcular la integral de la funci´on x1x
# 2
# 2x
# 3
# 3x
# 4
# 4x
# 5
# 5
# sobre el hipercubo J
# m de
# dimensi´on m = 5 en base a 106
# iteraciones. Calcular media, desviaci´on
# est´andar y un intervalo de confianza de nivel 95%.
# Comparar con los resultados obtenidos con el c´odigo del ejercicio 6.2.
# Sugerencia: definir 5 estratos, en funci´on del valor de x5, tomando los
# siguientes intervalos:
# [0, 0.72), [0.72, 0.83), [0.83, 0.90), [0.90, 0.95), [0.95, 1]. Hacer dos
# experimentos, uno tomando 106/5 iteraciones en cada estrato, otro
# tomando una cantidad de iteraciones proporcional a la probabilidad de
# cada estrato.
# Fecha entrega: Ver cronograma del curso.


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

def generate_html_table(estimacion_integral, estimacion_varianza_integral, intervalo_confianza, estimacion_varianza, tiempo_ejecucion):
    tabla_html = "<table><tr><th>Estimación</th><th>Varianza del estimador</th><th>Variaza de la integral</th><th>Intervalo de confianza</th><th>Tiempo de ejecución</th> </tr>"
    tabla_html += "<tr><td>" + str(estimacion_integral) + "</td><td>" + str(estimacion_varianza) + "</td><td>" + str(estimacion_varianza_integral) + "</td><td>" + str(intervalo_confianza) + "</td><td>" + str(tiempo_ejecucion) + "</td></tr>"
    tabla_html += "</table>"
    return tabla_html

def nN(epsilon, delta, estimacion_varianza):
    return math.ceil((stats.norm.ppf(1 - delta/2))**2 * (estimacion_varianza) / epsilon**2)

def f2(xAll):
    x1 = xAll[0]
    x2 = xAll[1]
    x3 = xAll[2]
    x4 = xAll[3]
    x5 = xAll[4]
    return (x1 * x2**2 * x3**3 * x4**4 * x5**5)

def calcularte_number_of_experiments_by_size(size_of_partition, size_of_domain, n):
    return math.ceil(size_of_partition * n / size_of_domain)

def calculate_Y(xAll):        
    #hago 1-xi para todas las entradas de xAll
    return [1 - xi for xi in xAll]

def IntegracionMonteCarloPorPartesfuncion(funcion, n, nivel_confianza, partitions, experiments_proportionals_to_size_of_partition):
    tiempo_inicial = time.time()

    arrayOut = []
    for p in range(0, len(partitions) - 1):
        partitionInit = partitions[p]
        partitionEnd = partitions[p+1]
        n_of_partition = 0

        if experiments_proportionals_to_size_of_partition:
            n_of_partition = calcularte_number_of_experiments_by_size(partitionEnd - partitionInit, 1, n)
            p_i = (partitionEnd - partitionInit)
        else:
            n_of_partition = math.ceil(n/len(partitions))
            p_i = 1/5

        
        S = 0
        T = 0
        for j in range(1, n_of_partition):
            x1 = random.uniform(0,1)
            x2 = random.uniform(0,1)
            x3 = random.uniform(0,1)
            x4 = random.uniform(0,1)
            if experiments_proportionals_to_size_of_partition:
                x5 = random.uniform(partitionInit, partitionEnd)
            else:
                x5 = random.uniform(p/5, (p+1)/5)
            
            xAll = [x1, x2, x3, x4, x5]
            yAll = calculate_Y(xAll)

            W = (funcion(xAll) + funcion(yAll))/2
            S += W
            if j > 1:
                T = T + (1-(1/j))*(W -  (S/(j-1)))**2


        

        estimacion_integral = S / n_of_partition * p_i
        estimacion_varianza = (T / (n_of_partition - 1)) * p_i**2
        estimacion_varianza_integral = estimacion_varianza / n_of_partition

        arrayOut.append([estimacion_integral, estimacion_varianza_integral, estimacion_varianza])
    

    sum_estimacion_integral = 0
    sum_estimacion_varianza_integral = 0
    sum_estimacion_varianza = 0
    for i in range(len(arrayOut)):
        sum_estimacion_integral += arrayOut[i][0]
        sum_estimacion_varianza_integral += arrayOut[i][1]
        sum_estimacion_varianza += arrayOut[i][2]
    
    tiempo_final = time.time()

    tiempo_ejecucion = tiempo_final - tiempo_inicial

    intervalo_de_confianza = Calculo_intervalo_de_confianza (1-nivel_confianza, sum_estimacion_integral,n, sum_estimacion_varianza)

    return  sum_estimacion_integral, sum_estimacion_varianza_integral, sum_estimacion_varianza, intervalo_de_confianza, tiempo_ejecucion
        



print("Ejercicio 14.1")
vreal = (1/2)*(1/3)*(1/4)*(1/5)*(1/6)
print("Valor real: ", vreal)
print ("---------------------------------")
print("Sin tomar encuenta el tamaño de las particiones")


particiones = [0, 0.72, 0.83, 0.90, 0.95, 1]

nivel_confianza = 0.95
delta = 1- nivel_confianza
estimacion_integral, estimacion_varianza_integral, estimacion_varianza,intervalo_de_confianza, tiempo_ejecucion = IntegracionMonteCarloPorPartesfuncion(f2, 10**6, nivel_confianza, particiones, False)

print("Estimación: ", estimacion_integral)
print("estimacion_varianza",estimacion_varianza)
print("estimacion_varianza_integral",estimacion_varianza_integral)
print("Intervalo de confianza: ", intervalo_de_confianza)
print("Tiempo de ejecución: ", tiempo_ejecucion)

print ("---------------------------------")
print("Tomando encuenta el tamaño de las particiones")
estimacion_integral, estimacion_varianza_integral, estimacion_varianza,intervalo_de_confianza, tiempo_ejecucion = IntegracionMonteCarloPorPartesfuncion(f2, 10**6, nivel_confianza, particiones, True)

print("Estimación: ", estimacion_integral)
print("estimacion_varianza",estimacion_varianza)
print("estimacion_varianza_integral",estimacion_varianza_integral)
print("Intervalo de confianza: ", intervalo_de_confianza)
print("Tiempo de ejecución: ", tiempo_ejecucion)

print ("---------------------------------")



# Estimacion 6.2
# Estimación:  0.001393239485866339
# estimacion_varianza 9.658300492263539e-05
# estimacion_varianza_integral 9.658300492263539e-11
# Número de muestras:  37102
# Parte 3
# Valor real:  0.0013888888888888887
# ---------------------------------
# Sin tomar encuenta el tamaño de las particiones
# Estimación:  0.0013778184874532436
# estimacion_varianza 8.85991811559816e-06
# estimacion_varianza_integral 5.315940237478422e-11
# Intervalo de confianza:  [0.001371984534197021, 0.0013836524407094663]
# Tiempo de ejecución:  2.5220184326171875
# ---------------------------------
# Tomando encuenta el tamaño de las particiones
# Estimación:  0.0013847332539588938
# estimacion_varianza 1.7901452171553825e-05
# estimacion_varianza_integral 4.530930774243382e-11
# Intervalo de confianza:  [0.0013764406252232244, 0.0013930258826945633]
# Tiempo de ejecución:  3.012700080871582