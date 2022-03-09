#reduccion.py
#cat result-diabetes.csv | python mapeo.py | python reduccion.py

import sys

salida = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    cod, valor = line.split('\t')
    # print (prueba, con)
    if cod in salida:
        salida[cod].append(int(valor))
    else:
        salida[cod] = []
        salida[cod].append(int(valor))

print(len(salida))

# for cod in salida.keys():
#     num_p = len(salida[cod])
#     # promedio = Average(salida[prueba])
#     print(f'{cod} : {num_p} ')