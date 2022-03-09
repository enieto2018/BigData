#reduccion.py
#cat result-diabetes.csv | python mapeo.py | python reduccion.py

import sys

salida = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    prueba, edad = line.split('\t')
    # print (prueba, con)
    if prueba in salida:
        salida[prueba].append(int(edad))
    else:
        salida[prueba] = []
        salida[prueba].append(int(edad))

# print(salida)

for prueba in salida.keys():
    cantidadEdades = len(salida[prueba])
    sumaEdades = sum(salida[prueba])
    promedioCalculado = sumaEdades / cantidadEdades
    # promedio = Average(salida[prueba])
    print(f'{prueba} : {promedioCalculado}')