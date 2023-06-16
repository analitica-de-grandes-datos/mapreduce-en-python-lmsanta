#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for l in sys.stdin:
    lista = l.split(',')
    purpose = lista[3]
    amount = lista[4]
    print(f"{purpose}\t{amount}")
