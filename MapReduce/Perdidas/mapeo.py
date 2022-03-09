#mapeo.py
import sys
#cat result-diabetes.csv | python mapeo.py
# entrada viene de STDIN (standard input)

try:
    enca = True
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")
        #print line        
        cod = line[8]
        num = line[9]
        
        if not enca:            
            print(f'{cod} \t {num}')

        enca = False
except:
    pass
