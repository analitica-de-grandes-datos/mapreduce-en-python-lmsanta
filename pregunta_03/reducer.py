#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

datos = []

for line in sys.stdin:
    key, value = line.strip().split('\t')
    clave = line[0].strip()
    valor = line[2].strip()
    datos.append((clave,valor))
    datos.sort(key= lambda x: (x[1],x[0]))

for item in datos:
    clave,valor = item
    print(f"{clave},{valor}")