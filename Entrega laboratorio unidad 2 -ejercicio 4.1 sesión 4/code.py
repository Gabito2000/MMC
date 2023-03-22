# Ejercicio
# Entrega 2 - Ejercicio 4.1 (individual):
# 1. Comparar y discutir la dependencia de los criterios de peor caso nC,
# nN, nH frente a los par´ametros ϵ y δ.
# 2. Calcular nC, nN, nH para ϵ = 0.01, δ = 0.001, 0.01, 0.05.
# Fecha entrega: ver el calendario en el EVA.



import math
import scipy.stats as stats
# import matplotlib.pyplotmatplotlib.pyplot as plt
# import numpy as np

# nC(ϵ, δ) = ⌈1/(4*δ*ϵ**2)⌉.
def nC(epsilon, delta):
    return math.ceil(1/(4*delta*epsilon**2))

# nN(ϵ, δ) =  ⌈(Φ^-1(1 − δ/2)/2*ϵ)^2⌉.
#donde Φ^-1 es la inversa de la distribución de la normal (0,1)
def nN(epsilon, delta):
    return math.ceil((stats.norm.ppf(1 - delta/2)/(epsilon*2))**2)

#nH(ϵ, δ) =  ⌈2*ln(2/δ)/(4*ϵ**2)⌉.
def nH(epsilon, delta):
    return math.ceil(2*math.log(2/delta)/(4*epsilon**2))

def giveFormatToArrayNumbers(arr):
    return ["{:,}".format( i ) for i in arr]


eps = [0.05, 0.01, 0.001]
delta = [0.5, 0.05, 0.005]

table = {}
table["nC"] = [nC(eps[0], delta[0]), nC(eps[0], delta[1]), nC(eps[0], delta[2]), nC(eps[1], delta[0]), nC(eps[1], delta[1]), nC(eps[1], delta[2]), nC(eps[2], delta[0]), nC(eps[2], delta[1]), nC(eps[2], delta[2])]
table["nN"] = [nN(eps[0], delta[0]), nN(eps[0], delta[1]), nN(eps[0], delta[2]), nN(eps[1], delta[0]), nN(eps[1], delta[1]), nN(eps[1], delta[2]), nN(eps[2], delta[0]), nN(eps[2], delta[1]), nN(eps[2], delta[2])]
table["nH"] = [nH(eps[0], delta[0]), nH(eps[0], delta[1]), nH(eps[0], delta[2]), nH(eps[1], delta[0]), nH(eps[1], delta[1]), nH(eps[1], delta[2]), nH(eps[2], delta[0]), nH(eps[2], delta[1]), nH(eps[2], delta[2])]

table["nC"] = giveFormatToArrayNumbers(table["nC"])
table["nN"] = giveFormatToArrayNumbers(table["nN"])
table["nH"] = giveFormatToArrayNumbers(table["nH"])

print (table)
# #crear tabla ejercicio 1
# open("output_table_e1.html","w", encoding="utf-8").write("<table> nC <tr> <td></td> <td> δ=" + str(delta[0]) + "</td> <td> δ=" + str(delta[1]) + "</td> <td> δ=" + str(delta[2]) + "</td> </tr> <tr> <td> ϵ=" + str(eps[0]) + "</td> <td> " + str(table["nC"][0]) + "</td> <td> " + str(table["nC"][1]) + "</td> <td> " + str(table["nC"][2]) + "</td> </tr> <tr> <td> ϵ=" + str(eps[1]) + "</td> <td> " + str(table["nC"][3]) + "</td> <td> " + str(table["nC"][4]) + "</td> <td> " + str(table["nC"][5]) + "</td> </tr> <tr> <td> ϵ=" + str(eps[2]) + "</td> <td> " + str(table["nC"][6]) + "</td> <td> " + str(table["nC"][7]) + "</td> <td> " + str(table["nC"][8]) + "</td> </tr> </table> <table> nN <tr> <td></td> <td> δ=" + str(delta[0]) + "</td> <td> δ=" + str(delta[1]) + "</td> <td> δ=" + str(delta[2]) + "</td> </tr> <tr> <td> ϵ=" + str(eps[0]) + "</td> <td> " + str(table["nN"][0]) + "</td> <td> " + str(table["nN"][1]) + "</td> <td> " + str(table["nN"][2]) + "</td> </tr> <tr> <td> ϵ=" + str(eps[1]) + "</td> <td> " + str(table["nN"][3]) + "</td> <td> " + str(table["nN"][4]) + "</td> <td> " + str(table["nN"][5]) + "</td> </tr> <tr> <td> ϵ=" + str(eps[2]) + "</td> <td> " + str(table["nN"][6]) + "</td> <td> " + str(table["nN"][7]) + "</td> <td> " + str(table["nN"][8]) + "</td> </tr> </table> <table> nH <tr> <td></td> <td> δ=" + str(delta[0]) + "</td> <td> δ=" + str(delta[1]) + "</td> <td> δ=" + str(delta[2]) + "</td> </tr> <tr> <td> ϵ=" + str(eps[0]) + "</td> <td> " + str(table["nH"][0]) + "</td> <td> " + str(table["nH"][1]) + "</td> <td> " + str(table["nH"][2]) + "</td> </tr> <tr> <td> ϵ=" + str(eps[1]) + "</td> <td> " + str(table["nH"][3]) + "</td> <td> " + str(table["nH"][4]) + "</td> <td> " + str(table["nH"][5]) + "</td> </tr> <tr> <td> ϵ =" + str(eps[2]) + "</td> <td> " + str(table["nH"][6]) + "</td> <td> " + str(table["nH"][7]) + "</td> <td> " + str(table["nH"][8]) + "</td> </tr> </table>")


#2. Calcular nC, nN, nH para ϵ = 0.01, δ = 0.001, 0.01, 0.05.
print ("ϵ = 0.01, δ = 0.001, 0.01, 0.05")

table = {}
table["nC"] = giveFormatToArrayNumbers([nC(0.01, 0.001), nC(0.01, 0.01), nC(0.01, 0.05)])
table["nN"] = giveFormatToArrayNumbers([nN(0.01, 0.001), nN(0.01, 0.01), nN(0.01, 0.05)])
table["nH"] = giveFormatToArrayNumbers([nH(0.01, 0.001), nH(0.01, 0.01), nH(0.01, 0.05)])



print (table)

# crear tabla ejercicio 2
# open("output.html","w", encoding="utf-8").write("<table> <tr> <th> </th> <th> nC </th> <th> nN </th> <th> nH </th> </tr> <tr> <td> ϵ = 0.01, δ = 0.001 </td> <td> " + str(table["nC"][0]) + "</td> <td> " + str(table["nN"][0]) + "</td> <td> " + str(table["nH"][0]) + "</td> </tr> <tr> <td> ϵ = 0.01, δ = 0.01 </td> <td> " + str(table["nC"][1]) + "</td> <td> " + str(table["nN"][1]) + "</td> <td> " + str(table["nH"][1]) + "</td> </tr> <tr> <td> ϵ = 0.01, δ = 0.05 </td> <td> " + str(table["nC"][2]) + "</td> <td> " + str(table["nN"][2]) + "</td> <td> " + str(table["nH"][2]) + "</td> </tr> </table>")

# # crear el grafico
# n_groups = 3
# nC = table["nC"]
# nN = table["nN"]
# nH = table["nH"]
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.20
# opacity = 0.9

# rects1 = plt.bar(index, nC, bar_width,alpha=opacity,color='g',label='nC')

# rects2 = plt.bar(index + bar_width, nN, bar_width,alpha=opacity,color='b',label='nN')

# rects3 = plt.bar(index + bar_width*2, nH, bar_width,alpha=opacity,color='r',label='nH')

# plt.xlabel('δ')
# plt.ylabel('n')
# plt.title('nC, nN, nH')
# plt.xticks(index + bar_width, ('0.001', '0.01', '0.05'))
# plt.legend()
# plt.tight_layout()
# plt.show()
# #save the graph
# fig.savefig("output.png")





