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

sumatoria =0
for cod in salida.keys():
    sumatoria = sumatoria + len(salida[cod])
    
numMunicipios = len(salida)
promedio = sumatoria/numMunicipios
print(f'{"RISARALDA"} : {promedio} ')