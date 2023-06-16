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
    key, value = line.strip().split(',')
    letras.append(key)
    numeros.append(int(value))
    datos = list(zip(letras,numeros))

lista = []
for clave,grupo in itertools.groupby(datos, lambda x : x[0]): 
    listanums = []
    for count in grupo:
        listanums.append(count[1])
    par = (clave, sorted(listanums))
    lista.append(par)

for item in lista:
    letra = ",".join(str(valor) for valor in (item[1]))
    print(f"{item[0]}\t{str(letra)}")