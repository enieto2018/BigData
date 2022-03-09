#mapeo.py
import sys
#cat result-diabetes.csv | python mapeo.py
# entrada viene de STDIN (standard input)

try:
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")
        #print line

        if len(line) ==10:
            edad = line[8]
            prueba = line[9]
	    if prueba=='tested_negative' or prueba=='tested_positive':
            	print '%s\t %s' % (edad, prueba)

except:
    pass
