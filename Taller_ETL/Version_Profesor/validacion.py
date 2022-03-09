import sys 
import db
from modelos import*

cont=0
try:
    encab=True
    for line in sys.stdin:
        line = line.strip()
        line = line.split(',')
        
        if not encab:
            if len(line[0])<=4:
                pass
            else:
                print('E101', line[0])
                cont+=1
        encab=False
except Exception as e:
    print(e)

print(f'cantidad de errores {cont}')
