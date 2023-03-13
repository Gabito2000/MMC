import random
import time
import statistics

# Definir tareas y sus tiempos aleatorios
tasks = {
    'T1': lambda: random.uniform(40, 56),
    'T2': lambda: random.uniform(24, 32),
    'T3': lambda: random.uniform(20, 40),
    'T4': lambda: random.uniform(16, 48),
    'T5': lambda: random.uniform(10, 30),
    'T6': lambda: random.uniform(15, 30),
    'T7': lambda: random.uniform(20, 25),
    'T8': lambda: random.uniform(30, 50),
    'T9': lambda: random.uniform(40, 60),
    'T10': lambda: random.uniform(8, 16)
}

# Definir dependencias entre tareas
dependencies = {
    'T2': ['T1'],
    'T3': ['T1'],
    'T4': ['T2', 'T3'],
    'T5': ['T2', 'T3'],
    'T6': ['T3'],
    'T7': ['T3'],
    'T8': ['T4', 'T5', 'T6', 'T7'],
    'T9': ['T5'],
    'T10': ['T7', 'T8', 'T9']
}

task_Time = dict()

def calculate_time(task):
    if task in task_Time:
        return task_Time[task]

    time = tasks[task]()
    time_dependences = 0
    if task in dependencies:
        for dependency in dependencies[task]:
            time_dependences = max(time_dependences, calculate_time(dependency))
    
    task_Time[task] = time + time_dependences
    return task_Time[task]

def calculate_total_time():
    task_Time.clear()
    max_time_to_end = 0
    for task in tasks:
       max_time_to_end = max(max_time_to_end, calculate_time(task))
    return max_time_to_end
    
def perform_simulation(n):
    start_time = time.time()
    X = [calculate_total_time() for i in range(n)]
    end_time = time.time()
    
    mean_time = 0 
    Vb = 0
    n = len(X)

    for i in range(n):
        mean_time += X[i] # Accumulate
        Vb += X[i]**2 # Accumulate

    mean_time /= n
    Vb = Vb / (n*(n-1)) - mean_time**2 / (n-1)
    stddev_time = Vb**0.5

    return mean_time, stddev_time, end_time - start_time



# Pedir la cantidad de replicaciones
n = int(input("Ingrese la cantidad de replicaciones a realizar: "))


# Iniciar el tiempo de cálculo del programa
mean_time, stddev_time, compute_time = perform_simulation(n)


# Mostrar los resultados y el tiempo de cálculo empleado por el programa
print(f"La media del tiempo total de construcción es {mean_time:.9f} horas.")
print(f"La desviación estándar del tiempo total de construcción es {stddev_time:.9f} horas.")
print(f"El tiempo de cálculo del programa fue de { compute_time:.9f} segundos.")

# generat the output file with the results of the simulation of Monte Carlo
# Utilizar el programa con n = 10, 10^2
# , 10^3
# , 10^4
# , 10^5
# , 10^6
# , y mostrar en
# una tabla las estimaciones de media y desviaci´on est´andar, as´ı como los
# tiempos de c´alculo. Discutir estos resultados. (en caso que el tiempo de
# ejecuci´on para 106
# replicaciones sea menor que 60 segundos, agregar
# experimentos con mayor n´umero de iteraciones, siempre multiplicando
# por 10, hasta que uno de los experimentos supere esa duraci´on)

with open("output.html", "w") as file:
    file.write("<table>")
    file.write("<tr><th>n</th><th>mean</th><th>sqrt(Var_X)</th><th></th><th>time</th></tr>")
    i = 0
    # for n in [10, 10**2, 10**3, 10**4, 10**5, 10**6]:
    compute_time = 0
    while i < 6 or compute_time < 60:
        i += 1
        n = 10**i
        mean_time, stddev_time, compute_time = perform_simulation(n)

        file.write(f"<tr><td>10^{i}</td><td>{mean_time:.9f}</td><td>{stddev_time:.9f}</td><td>{compute_time:.9f}</td></tr>")

    file.write("</table>")
