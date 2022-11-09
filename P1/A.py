"""
Implementar y llevar a cabo su an ́alisis aposteriori tanto para el mejor caso comopara  el  peor  caso  de  un  algoritmo  que  realice  la  siguiente  tarea:  
Considere  un  arreglo  deenterosA[0, ..., n−1] con valores random entre 0 y 3n. 
Si los valores del arreglo son tal que,
si alguno de los valores en el subarregloA[0, ..., n/2] se encuentra tambi ́en en el subarregloA[n/2 + 1, ..., n−1], 
 entonces  el  algoritmo  devolver ́a  el  valor  que  se  encuentra  en  ambossubarreglos y sus posiciones respectivamente en cada subarreglo. 
 Si el algoritmo encuentra unelemento con estas caracter ́ısticas, 
entonces, se detendr ́a mostrando  ́unicamente el primeroque  cumpla  la  condicion. 
"""

"""
Desarrolado por A.M
Análisis de algoritmos 3CV11

"""
import numpy as np


tam=int(input("Ingrese un número para el tamanio del arreglo"))
print("los datos capturados son:\n tam=", tam )

x=[]

for i in range(tam):
    number=np.random.randint(0, (tam*3))
    x.append(number)
print(x)
    

