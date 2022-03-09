import sys
import db
from modelos import *

try:
    ban = 0
    for line in sys.stdin:
        # Separando datos del archivo de muestra teniendo en cuenta la coma (archivo .CSV)
        line = line.strip()
        line = line.split(',')

        # Bandera para evitar el recorrido de la primera linea (encabezados del archivo)
        if ban > 0:        
            # Guardando columnas en variables
            objectId = line[0]
            pet_cod_depto = line[6]
            pet_dpto = line[7]

            #Imprimiento valores a guardar
            print(objectId, pet_cod_depto, pet_dpto)
            # Crear conexion base de datos
            db.Base.metadata.create_all(db.motor)
            # Crear informacion a guardar
            depts=Departamento(objectid=objectId, pet_cod_depto=pet_cod_depto, pet_dpto=pet_dpto)
            # Abrir conexion y guardar
            db.session.add(depts)
            db.session.commit()
        # Igualando ban a 1 para que no aumente mas y evitar uso innecesario    
        if ban == 0 : ban=1
except Exception as e:
    # Imprimiendo excepción
    print(e)