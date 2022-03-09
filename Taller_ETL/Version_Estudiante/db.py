from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

motor = create_engine("postgresql+psycopg2://postgres:Pasa.123@localhost:5432/PQRSalud")
Session= sessionmaker(bind=motor)
session= Session()
Base= declarative_base()
