
# Ejercicio 3.1 (sesión 3)
# Problema: se desea estimar el volumen de una regi´on R de [0, 1]6 definida
# por todos los puntos de la hiper-esfera de centro
# (0.45, 0.5, 0.6, 0.6, 0.5, 0.45) y radio 0.35, que adem´as cumplan las
# restricciones siguientes: 3x1 + 7x4 ≤ 5; x3 +x4 ≤ 1; x1 −x2 −x5 +x6 ≥ 0.
# Entrega 2 - Ejercicio 3.1 (individual)
# • Parte a: implementar un programa que reciba como par´ametro la
# cantidad de replicaciones n a realizar, y emplee Monte Carlo para
# calcular (e imprimir) la estimaci´on del volumen de R, y la desviaci´on
# est´andar de este estimador. Incluir c´odigo para calcular el tiempo de
# c´alculo empleado por el programa. Utilizar el programa con n = 104
# y
# luego con n = 106 para estimar el volumen de R. Discutir si los dos
# valores obtenidos parecen consistentes.
# (en la sesi´on 5 se continuar´a este ejercicio).
# • Parte b: como forma de validar el programa, eliminar las restricciones
# Curso “M´etodos de Monte Carlo” - Facultad de Ingenier´ıa, Universidad de la Rep´ublica (Uruguay) 23
# adicionales de desigualdad, y comparar el volumen calculado por Monte
# Carlo con n = 106
# con el valor exacto del volumen de una hiperesfera
# de dimensi´on 6, π
# 3
# r
# 6/6
# (https://web.archive.org/web/20190915215955/http:
# //www.sjsu.edu/faculty/watkins/ndim.htm - versi´on archivada, el
# original http://www.sjsu.edu/faculty/watkins/ndim.htm ya no est´a
# disponible). Discutir tambi´en la relaci´on de este valor con el obtenido
# en la parte a.
# Comentario: la hiperesfera de dimensi´on k, centro (c1, . . . ck) y radio r es
# el conjunto de puntos que verifican Pk
# i=1(xi − ci)
# 2 ≤ r
# 2
# .
# Fecha entrega: ver el calendario en el EVA.


import random
import math
import sys
import time

random.seed(1402)

ejecutar_solo_una_parte = len(sys.argv) == 3

# Declare the required variables
if not ejecutar_solo_una_parte:
    print("Se ejecutarán todos los problemas.\nPara ver el resultado de un problema específico: python code.py tamaño_de_muesta tiene_restricciones(y/n)\n example: python code.py 10000 y")


c1 = 0.45
c2 = 0.5
c3 = 0.6
c4 = 0.6
c5 = 0.5
c6 = 0.45
r = 0.35

generar_tabla = False

def calculateVolume(tamaño_de_muesta, tiene_restricciones):
    estimado = 0

    for i in range(tamaño_de_muesta):
        # Generar las coordenadas de un punto aleatorio en el cubo [0, 1]^6
        x1, x2, x3, x4, x5, x6 = random.random(), random.random(), random.random(), random.random(), random.random(), random.random()

        # If está dentro de la esfera
        if ((x1 - c1)**2 + (x2 - c2)**2 + (x3 - c3)**2 + (x4 - c4)**2 + (x5 - c5)**2 + (x6 - c6)**2) <= r**2:
            if tiene_restricciones:
                if (3*x1 + 7*x4 <= 5) and (x3 + x4 <= 1) and (x1 - x2 - x5 + x6 >= 0):
                    estimado += 1
            else:
                estimado += 1
    
    # Normalizar el estimado
    estimado /= tamaño_de_muesta

    estimado_desviación = math.sqrt(estimado * (1 - estimado) / (tamaño_de_muesta - 1))

    return estimado, estimado_desviación

def calculateExactVolume():
    volumenExacto = math.pi**(6/2) * r**6 / 6
    print("Volumen exacto:", volumenExacto)
    return volumenExacto

resultados = {}
def ejecutarParte( parte, tamaño_de_muesta, tiene_restricciones):
        start_time = time.time()
        retultado = calculateVolume(tamaño_de_muesta, tiene_restricciones)
        tiempo_de_ejecucion = time.time() - start_time
        resultados[parte] = [retultado[0], retultado[1], tiempo_de_ejecucion]
        print("Parte", parte, "tiempo de ejecución:", tiempo_de_ejecucion, "seconds")
        print("estimado:", retultado[0], "estimado_desviación:", retultado[1])
        return retultado

if ejecutar_solo_una_parte:
    ejecutarParte("Input_"+str(sys.argv[1])+"_"+str(sys.argv[2]), int(sys.argv[1]), sys.argv[2] == "y")
    open("resultados"+str(sys.argv[1])+"_"+str(sys.argv[2])+".html", "w").write("<table><tr><th>Parte</th><th>Estimado</th><th>Estimado Desviación</th><th>Tiempo de ejecución</th></tr> <tr><td>"+str(sys.argv[1])+"_"+str(sys.argv[2])+"</td><td>"+str(resultados["Input_"+str(sys.argv[1])+"_"+str(sys.argv[2])][0])+"</td><td>"+str(resultados["Input_"+str(sys.argv[1])+"_"+str(sys.argv[2])][1])+"</td><td>"+str(resultados["Input_"+str(sys.argv[1])+"_"+str(sys.argv[2])][2])+"</td></tr></table>")

else:
    ejecutarParte("A1", 10000, True)

    ejecutarParte("A2", 1000000, True)

    ejecutarParte("B", 1000000, False)
    
    volumenExacto = calculateExactVolume()
    
    print ("Resultados:")
    for key in resultados:
        print(key, "estimado:", resultados[key][0], "estimado_desviación:", resultados[key][1], "tiempo_de_ejecución:", resultados[key][2])
    print ("Volumen exacto:", volumenExacto)
    if generar_tabla:
        open("tabla_ejercicio_3_1.html", "w").write("<table>Ejercicio A<tr><td></td> <td>Estimado</td><td>Desviación estándar</td><td>Tiempo de ejecución</td></tr><tr><td>A1</td><td>" + str(resultados["A1"][0]) + "</td><td>" + str(resultados["A1"][1]) + "</td><td>" + str(resultados["A1"][2]) + "</td></tr><tr><td>A2</td><td>" + str(resultados["A2"][0]) + "</td><td>" + str(resultados["A2"][1]) + "</td><td>" + str(resultados["A2"][2]) + "</td></tr></table><table>Ejercicio B<tr><td>Valor calculado</td><td>Valor_exacto</td><td>Porcentaje de error</td><td>Desviación estándar</td></tr><tr><td>" + str(resultados["B"][0]) + "</td><td>" + str(volumenExacto) + "</td><td>" + str((abs(resultados["B"][0] - volumenExacto)) / volumenExacto * 100) + "%</td><td>" + str(resultados["B"][1]) + "</td></tr></table>")
        
