#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import itertools
from operator import itemgetter

datos = []
letras = []
numeros = []


for line in sys.stdin:
    key, value = line.strip().split('\t')
    letras.append(key)
    numeros.append(float(value))
    datos = list(zip(letras,numeros))

lista = []
for clave,grupo in itertools.groupby(datos, lambda x : x[0]): 
    listanums = []
    for count in grupo:
        listanums.append(count[1])
    trio = (clave, max(listanums), min(listanums))
    lista.append(trio)

for item in lista:
    clave, maximo, minimo = item
    print(f"{clave}\t{maximo}\t{minimo}")