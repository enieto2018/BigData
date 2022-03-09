import db
from modelos import *

def Insertar(objectid, pet_cod_depto, pet_dpto):
        depts=Departamento(objectid=objectid, pet_cod_depto=pet_cod_depto, pet_dpto=pet_dpto)
        db.session.add(depts)
        db.session.commit()
        
db.Base.metadata.create_all(db.motor)

 