#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for l in sys.stdin:
    lista = l.split(',')
    clave = lista[0].strip()
    valor = int(lista[1].strip())
    print(f"{clave}\t{valor}")