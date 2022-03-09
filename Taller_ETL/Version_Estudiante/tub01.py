import sys
import principal

def recorrer_for():
    for line in sys.stdin:
        line = line.strip()
        line = line.split(',')
        objectId = line[0]
        pet_cod_depto = line[6]
        pet_dpto = line[7]
        print(line[0])
        print(line[6])
        print(line[7])

        if(objectId!= "objectId" and pet_cod_depto!="pet_cod_depto" and pet_dpto!="pet_dpto"):
            principal.Insertar(objectId, pet_cod_depto, pet_dpto)
    
# principal.Insertar
recorrer_for()