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

import math
import scipy.stats as stats
import time
import sys

txt_con_tabla_de_random = "Entrega laboratorio unidad 4 -ejercicio 8.1/random3.txt" # SI SE CAMBIA POR RANDdigits.TXT DESCOMENTAR LA LINEA 47
random_arr = []
# cargar tabla de random en un array
with open(txt_con_tabla_de_random) as f:
    random_arr = f.readlines()

#separate by line
random_arr = [x.strip() for x in random_arr]

#separate by space
random_arr = [x.split(" ") for x in random_arr]

#remove the index
# random_arr = [x[1:] for x in random_arr]

#remove all empty strings
random_arr = [list(filter(None, x)) for x in random_arr]

#make one big array
random_arr = [item for sublist in random_arr for item in sublist]

#convert to float
random_arr = [float(x) for x in random_arr]

#convert between 0 and 1
random_arr = [x/(10**5) for x in random_arr]

print("Se cargó la tabla de random con {} valores".format(len(random_arr)))

cantidad_de_elementos = len(random_arr)

random = {
    "index": 0,
    "get": lambda: random_arr[random["index"]],
    "next": lambda: random["index"] + 1,
    "random": lambda a, b: a + (b - a) * random["get"](),
}

# Define a new function that increments the index and returns the corresponding value from random_arr
def get_next():
    value = random_arr[random["index"]]
    random["index"] = (random["index"] + 1) % (len(random_arr)-1)
    # if random["index"] == 0:
    #     print("Se acabó la tabla de random")
    return value
    

# Replace the "get" method with the new function
random["get"] = get_next

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
        x1, x2, x3, x4, x5, x6 = random["random"](0,1), random["random"](0,1), random["random"](0,1), random["random"](0,1), random["random"](0,1), random["random"](0,1)

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

    ejecutarParte("A2", cantidad_de_elementos, True)

    ejecutarParte("B", cantidad_de_elementos, False)
    
    volumenExacto = calculateExactVolume()
    
    print ("Resultados:")
    for key in resultados:
        print(key, "estimado:", resultados[key][0], "estimado_desviación:", resultados[key][1], "tiempo_de_ejecución:", resultados[key][2])
    print ("Volumen exacto:", volumenExacto)
    if generar_tabla:
        open("tabla_ejercicio_3_1.html", "w").write("<table>Ejercicio A<tr><td></td> <td>Estimado</td><td>Desviación estándar</td><td>Tiempo de ejecución</td></tr><tr><td>A1</td><td>" + str(resultados["A1"][0]) + "</td><td>" + str(resultados["A1"][1]) + "</td><td>" + str(resultados["A1"][2]) + "</td></tr><tr><td>A2</td><td>" + str(resultados["A2"][0]) + "</td><td>" + str(resultados["A2"][1]) + "</td><td>" + str(resultados["A2"][2]) + "</td></tr></table><table>Ejercicio B<tr><td>Valor calculado</td><td>Valor_exacto</td><td>Porcentaje de error</td><td>Desviación estándar</td></tr><tr><td>" + str(resultados["B"][0]) + "</td><td>" + str(volumenExacto) + "</td><td>" + str((abs(resultados["B"][0] - volumenExacto)) / volumenExacto * 100) + "%</td><td>" + str(resultados["B"][1]) + "</td></tr></table>")
        
