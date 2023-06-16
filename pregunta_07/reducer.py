#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

datos = []

for line in sys.stdin:
    key, date, value = line.strip().split('\t')
    datos.append((key, date, int(value)))
    datos.sort(key = lambda x: (x[0], x[2], x[1]))

for item in datos:
    clave, date, value = item
    print(f"{clave}   {date}   {value}")