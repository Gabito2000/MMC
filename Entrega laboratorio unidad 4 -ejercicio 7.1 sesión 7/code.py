# Entrega 4
# Ejercicio 7.1 (individual):
# Problema: supongamos que un programa de posgrado incluye un conjunto
# de P profesores y otro de S estudiantes, y que se desea asignar a cada
# estudiante un profesor para consultas, pero que todas las personas son de
# diferentes pa´ıses y comprenden distintos idiomas. Si cada estudiante tiene
# asignado un profesor para consultas, la cantidad total de formas de asignar
# profesores a los estudiantes es P
# S (hay P opciones para cada estudiante, y
# S estudiantes en total, la cantidad total de opciones es el producto sobre
# los estudiantes de las opciones de cada estudiante).
# Supongamos que nos interesa determinar cuantas formas hay de asignar
# profesores a los estudiantes, respetando que cada profesor asignado a un
# estudiante tenga un idioma en com´un con él (para que puedan
# comunicarse). Si hay L lenguajes posibles, podemos tener para cada
# estudiante s un subconjunto Id(s) con los lenguajes que entiende, y lo
# mismo para cada profesor p; y una asignaci´on s´olo ser´ıa v´alida si para cada
# 16
# estudiante s y su profesor p(s), se cumple que Id(s) ∩ Id(p(s)) ̸= ∅ (estos
# conjuntos también podr´ıan representarse como matrices Ids,l e Idp,l, con
# entradas 1 cuando ese estudiante o profesor entienden el lenguaje l y 0 si
# no).
# Para estimar la cantidad de formas distintas de realizar estas asignaciones
# de profesores y estudiantes, es posible aplicar el método Monte Carlo.
# Se debe recibir en entrada el n´umero de replicaciones a realizar, y el nivel
# de confianza; en salida, se debe dar la estimaci´on del n´umero de
# combinaciones NC, as´ı como la desviaci´on est´andar y un intervalo de
# confianza (del nivel especificado) calculado en base al criterio de
# Agresti-Coull.
# • Parte a: escribir un programa para hacer el c´alculo previamente
# descrito. Entregar seudoc´odigo y c´odigo.
# • Parte b: sea el siguiente caso: Estudiantes/lenguajes: Maria: español,
# ingles; Sophie: inglés, francés; Liliana: español, portugués; Lucia:
# 17
# inglés, portugués; Monique: francés; Rodrigo: español, inglés, francés;
# John: inglés; Neymar: portugués, español; Jacques: francés, portugués;
# Juan: español. Profesores: Tom: inglés, frances, español; Luciana:
# inglés, portugués; Gerard: inglés, francés; Silvia: español, francés.
# Usando el programa anterior, y empleando 1000 replicaciones de Monte
# Carlo, estimar los valores de cuantas combinaciones NC hay para
# asignar profesores a estudiantes y que tengan un idioma en com´un, con
# intervalos de confianza de nivel 95%.
# • Parte c: adaptar el programa para calcular el n´umero de combinaciones
# si adem´as queremos agregar como restricci´on que ning´un profesor
# atienda menos de un estudiante ni m´as de cuatro estudiantes.
# Usando el programa modificado, y empleando 1000 replicaciones de
# Monte Carlo, estimar los valores de cuantas combinaciones NC hay para
# asignar profesores a estudiantes y que tengan un idioma en com´un y
# cuplan la restricci´on adicional mencionada, con intervalos de confianza
# de nivel 95%.


import random
from scipy import stats
import time

random.seed(1402)
create_output = False

def  Agresti_Coull(delta, estimado, n):
    def k(delta):
        return stats.norm.ppf(1 - (delta/2))

    S = estimado * n

    p = estimado

    q = 1-p

    x_mono = S + ((k(delta)**2) /2)

    n_mono = n + (k(delta)**2)

    p_mono = x_mono/n_mono

    q_mono = 1-p_mono

    CI_i = p - k(delta) * ((p_mono*q_mono)**0.5  ) * n_mono**(-1/2)

    CI_f = p + k(delta) * ((p_mono*q_mono)**0.5  ) * n_mono**(-1/2) 

    return CI_i, CI_f

def MonteCarloConteo(Profesores, Estudiantes, n, delta, conCupo = False):
    # r es la cantidad de combinaciones es decir Profesores * Estudiantes

    def cantidad_combinaciones(pelotas, cajas):

        # numerated balls in numerated boxes
        # return  math.factorial(pelotas) / (math.factorial(cajas) / math.factorial(pelotas - cajas))

        return cajas ** pelotas

    r = cantidad_combinaciones( len(Estudiantes), len(Profesores))
    S = 0
    if conCupo == True:
        cupo = 4
            
    for i in range(n):
        #Sorteamos todos los alumnos a ver a que profesor van
        S = S + 1 #Asumimos que la combinacion es valida
        profesores_cupo = {profesor: 0 for profesor in Profesores}
        for estudiante in Estudiantes:
            profesor = random.choice(list(Profesores.keys())) 
            #Vemos si el profesor tiene algun idioma en comun con el estudiante
            if (not any(Ip == 1 and Ie == 1 for Ip, Ie in zip(Profesores[profesor], Estudiantes[estudiante]))): 
                S = S-1 #Si no tiene idioma en comun, la combinacion no es valida
                break

            if conCupo == True:
                profesores_cupo[profesor] = profesores_cupo[profesor] + 1
                if profesores_cupo[profesor] > cupo:
                    S = S-1 #Si el profesor tiene mas de 4 alumnos, la combinacion no es valida
                    break

    integral = r*(S/n)
    varianza_integral = integral*(r-integral)/(n-1)

    intervalo = Agresti_Coull(delta, integral/r, n)

    intervalo = [intervalo[0]*r, intervalo[1]*r]

    return integral, varianza_integral**0.5,  intervalo
        

idiomas = ["español", "ingles", "frances", "portugues"]

estudiantes = {
    "Maria": [1, 1, 0, 0],
    "Sophie": [0, 1, 1, 0],
    "Liliana": [1, 0, 0, 1],
    "Lucia": [0, 1, 0, 1],
    "Monique": [0, 0, 1, 0],
    "Rodrigo": [1, 1, 1, 0],
    "John": [0, 1, 0, 0],
    "Neymar": [1, 0, 0, 1],
    "Jacques": [0, 0, 1, 1],
    "Juan": [1, 0, 0, 0]
}

profesores = {
    "Tom": [1, 1, 1, 0],
    "Luciana": [0, 1, 0, 1],
    "Gerard": [0, 1, 1, 0],
    "Silvia": [1, 0, 1, 0]
}

def print_idiomas_de_grupo(grupo, enum_idiomas):
    for nombre, idiomas in grupo.items():
        print(nombre, ": ", end="")
        for i in range(len(idiomas)):
            if idiomas[i] == 1:
                print(enum_idiomas[i], end=", ")
        print()



# Estudiantes/lenguajes: Maria: español,
# ingles; Sophie: inglés, francés; 
# Liliana: español, portugués; 
# Lucia:inglés, portugués; 
# Monique: francés; 
# Rodrigo: español, inglés, francés;
# John: inglés; 
# Neymar: portugués, español; 
# Jacques: francés, portugués;
# Juan: español. 
# 
# Profesores: Tom: inglés, frances, español; Luciana:
# inglés, portugués; Gerard: inglés, francés; Silvia: español, francés.

def crear_tabla_html(headers, datos):
    html = "<table border='1'>"
    html += "<tr>"
    for header in headers:
        html += f"<th>{header}</th>"
    html += "</tr>"
    for fila in datos:
        html += "<tr>"
        for dato in fila:
            html += f"<td>{dato}</td>"
        html += "</tr>"
    html += "</table>"
    return html

print ("Parte b")
print ("Estudiantes")
print_idiomas_de_grupo(estudiantes, idiomas)

print ("Profesores")
print_idiomas_de_grupo(profesores, idiomas)

print ("Parte b")
print ("Estimacion NC, desviación estándar, intervalo de confianza, tiempo de ejecucion")
tiempo_inicial = time.time()
resultados = MonteCarloConteo(profesores, estudiantes, 1000, 0.05)
tiempo_final = time.time()
tiempo_ejecucion = tiempo_final - tiempo_inicial
print(resultados, tiempo_ejecucion)

#printear en output
if create_output:
    output = open("output.html", "w")

    output.write(crear_tabla_html(["Estimacion NC", "desviación estándar", "intervalo de confianza", "tiempo de ejecucion"], [resultados + (tiempo_ejecucion,)]))






print("Parte c")
print ("Estimacion NC, desviación estándar, intervalo de confianza, tiempo de ejecucion")
tiempo_inicial = time.time()
resultados = MonteCarloConteo(profesores, estudiantes, 1000, 0.05, True)
tiempo_final = time.time()
tiempo_ejecucion = tiempo_final - tiempo_inicial
print(resultados, tiempo_ejecucion)

if create_output:
    output.write(crear_tabla_html(["Estimacion NC", "desviación estándar", "intervalo de confianza", "tiempo de ejecucion"], [resultados + (tiempo_ejecucion,)]))
