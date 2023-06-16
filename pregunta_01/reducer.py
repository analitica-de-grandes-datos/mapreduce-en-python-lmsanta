#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
count = 0
for line in sys.stdin:
    key, value = line.strip().split('\t')
    if key != current_key:
        if current_key is not None:
            print(f"{current_key}\t{count}")
        current_key = key
        count = 0

    #Incrementar el contador
    count += int(value)

# Imprimir el último resultado parcial
if current_key is not None:
    print(f"{current_key}\t{count}")