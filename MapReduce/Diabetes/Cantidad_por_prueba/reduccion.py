#reduccion.py
#cat result-diabetes.csv | python mapeo.py | python reduccion.py

import sys

salida = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    prueba, con = line.split('\t')
    # print (prueba, con)
    if prueba in salida:
        salida[prueba].append(int(con))
    else:
        salida[prueba] = []
        salida[prueba].append(int(con))

# print(salida)

for prueba in salida.keys():
    num_p = len(salida[prueba])
    print(f'{prueba} : {num_p}')