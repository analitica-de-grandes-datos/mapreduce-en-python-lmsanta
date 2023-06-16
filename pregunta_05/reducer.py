#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from collections import Counter

datos = []

for line in sys.stdin:
    key = line.strip().split('\n')
    datos.append(key)
    registros = sorted(list(Counter([x[0] for x in datos]).items()))

for item in registros:
    clave,valor = item
    print(f"{clave}\t{valor}")