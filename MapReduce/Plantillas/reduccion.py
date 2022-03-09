#reduccion.py
#cat result-diabetes.csv | python mapeo.py | python reduccion.py

import sys

salida = {}

#Partitoner
for line in sys.stdin:
    line = line.strip()
    edad, diag = line.split('\t')
    #print edad, diag
    if diag in salida:
        salida[diag].append(int(edad))
    else:
        salida[diag] = []
        salida[diag].append(int(edad))

#Reducer
print salida
acum=0
for diag in salida.keys():
    num_p = len(salida[diag])
    acum+=num_p
    ls_edades=salida[diag]
    sume=0
    for e in ls_edades:
      sume+=e
    prome=sume/num_p
    print '%s\t%s'% (diag, prome)
print 'total: ',acum




