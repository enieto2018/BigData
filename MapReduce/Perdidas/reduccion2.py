#reduccion.py
#cat result-diabetes.csv | python mapeo.py | python reduccion.py

import sys

salida = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    prueba, con = line.split('\t')
    #print edad, diag
    if prueba in salida:
        salida[prueba].append(int(con))
    else:
        salida[prueba] = []
        salida[prueba].append(int(con))

#Reducer
#print(salida)
acum=0
for prueba in salida.keys():
    num_p = len(salida[prueba])
    acum+=num_p
    # ls_edades=salida[prueba]
    # sume=0
    # for e in ls_edades:
    #   sume+=e
    # prome=sume/num_p
    print (f'{prueba} {num_p}')
# print('total: ', acum)




