#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for l in sys.stdin:
  lista = l.split(",")
  credit_history = lista[2]
  print(f"{credit_history}\t1")