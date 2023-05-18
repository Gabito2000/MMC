import random
import math
import sys
import time
random.seed(1402)
ejecutar_solo_una_parte = len(sys.argv) == 3
# Declare the required variables
if not ejecutar_solo_una_parte:
    print("Se ejecutar ́an todos los problemas.\nPara ver el resultado de un problema espec ́ıfico: python code.py tamaño_de_muesta tiene_restricciones(y/n)\n example: python code.py 10000 y")

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
        # If est ́a dentro de la esfera
        if ((x1 - c1)**2 + (x2 - c2)**2 + (x3 - c3)**2 + (x4 - c4)**2 + (x5 - c5)**2 + (x6 - c6)**2) <= r**2:
            if tiene_restricciones:
                if (3*x1 + 7*x4 <= 5) and (x3 + x4 <= 1) and (x1 - x2 - x5 + x6 >= 0):
                    estimado += 1
            else:
                estimado += 1


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
    open("resultados"+str(sys.argv[1])+"_"+str(sys.argv[2])+".html", "w").write("<table><tr><th>Parte</th><th>Estimado</th><th>Estimado Desviaci ́on</th><th>Tiempo de ejecución</th></tr> <tr><td>"+str(sys.argv[1])+"_"+str(sys.argv[2])+"</td><td>"+str(resultados["Input_"+str(sys.argv[1])+"_"+str(sys.argv[2])][0])+"</td><td>"+str(resultados["Input_"+str(sys.argv[1])+"_"+str(sys.argv[2])][1])+"</td><td>"+str(resultados["Input_"+str(sys.argv[1])+"_"+str(sys.argv[2])][2])+"</td></tr></table>")
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
            open("tabla_ejercicio_3_1.html", "w").write("<table>Ejercicio A<tr><td></td> <td>Estimado</td><td>Desviaci ́on est ́andar</td><td>Tiempo de ejecución</td></tr><tr><td>A1</td><td>" + str(resultados["A1"][0]) + "</td><td>" + str(resultados["A1"][1]) + "</td><td>" + str(resultados["A1"][2]) + "</td></tr><tr><td>A2</td><td>" + str(resultados["A2"][0]) + "</td><td>" + str(resultados["A2"][1]) + "</td><td>" + str(resultados["A2"][2]) + "</td></tr></table><table>Ejercicio B<tr><td>Valor calculado</td><td>Valor_exacto</td><td>Porcentaje de error</td><td>Desviaci ́on est ́andar</td></tr><tr><td>" + str(resultados["B"][0]) + "</td><td>" + str(volumenExacto) + "</td><td>" + str((abs(resultados["B"][0] - volumenExacto)) / volumenExacto * 100) + "%</td><td>" + str(resultados["B"][1]) + "</td></tr></table>")
