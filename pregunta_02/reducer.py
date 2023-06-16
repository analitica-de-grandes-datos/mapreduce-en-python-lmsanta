#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key = None
validator = 0

for line in sys.stdin:
    key,value = line.strip().split('\t')
    if key == current_key:
        if int(value) > validator:
            validator = max(validator, int(value))
    else:
        if current_key is not None:
            print(f"{current_key}\t{validator}")
        current_key = key
        validator = int(value)

#Imprimir el primer reultado parcial
if current_key is not None:
    print(f"{current_key}\t{validator}")
