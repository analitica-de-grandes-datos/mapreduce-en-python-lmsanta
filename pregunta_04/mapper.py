#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for l in sys.stdin:
    lista = l.split(" ")
    clave = lista[0]
    print(f"{clave}")