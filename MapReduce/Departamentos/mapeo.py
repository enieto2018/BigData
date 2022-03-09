import sys
#cat result-diabetes.csv | python mapeo.py
# entrada viene de STDIN (standard input)

try:
    encab=True
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")
        #print line
        cod = line[6]
        mun = line[9]

        if not encab:
            print(f'{cod}\t 1')
            
        encab = False
except:
    pass


