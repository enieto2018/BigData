import db
import psycopg2
from sqlalchemy import Column, Integer, Text, String

class Departamento(db.Base):
    __tablename__='departamento'
    objectid=Column(String(4), primary_key=True)
    pet_cod_depto=Column('cod_dpto', Integer)
    pet_dpto=Column('dpto', Text)