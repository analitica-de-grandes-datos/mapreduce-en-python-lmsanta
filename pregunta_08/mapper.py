#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for l in sys.stdin:
    lista = l.split(" ")
    letra = lista[0]
    valor = int(lista[6])
    print(f"{letra}\t{valor}")