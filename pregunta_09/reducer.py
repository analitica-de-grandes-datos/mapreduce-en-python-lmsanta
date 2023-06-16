#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from operator import itemgetter

datos = []

for line in sys.stdin:
    key, date, value = line.strip().split('\t')
    datos.append((key, date, int(value)))
    datos.sort(key = itemgetter(2))

for item in datos:
    clave, date, value = item
    if value <= 7:
        print(f"{clave}   {date}   {value}")