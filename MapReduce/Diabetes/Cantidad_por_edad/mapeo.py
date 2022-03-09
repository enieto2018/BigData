# import sys

# try:
#     for line in sys.stdin:
#         # Separando datos del archivo de muestra teniendo en cuenta la coma (archivo .CSV)
#         line = line.strip()
#         line = line.split(',')
#         print(line)
#         edad = line[8]
#         prueba = line[9]
#         print (edad,prueba)
# # except Exception as e:
# #     # Imprimiendo excepción
# #     print(e)
# except:
#     pass

#mapeo.py
import sys
#cat result-diabetes.csv | python mapeo.py
# entrada viene de STDIN (standard input)

try:
    encab=True
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")
        #print line
        edad = line[8]
        prueba = line[9]

        if not encab:
            # print(f'{edad}\t {prueba}')
            print(f'{prueba}\t {edad}')
        encab = False
except:
    pass