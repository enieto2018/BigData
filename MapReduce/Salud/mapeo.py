import sys
#cat result-diabetes.csv | python mapeo.py
# entrada viene de STDIN (standard input)

try:
    encab=True
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")
        #print line
        cod = line[7]
        mun = line[9]

        if not encab:
            # print(f'{edad}\t {prueba}')
            if(cod == "RISARALDA"):
                print(f'{mun}\t 1')
        encab = False
except:
    pass