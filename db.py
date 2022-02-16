from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine ("sqlite:///database/discos.db", connect_args={"check_same_thread":False})
engine = create_engine ("sqlite:///database/libros.db", connect_args={"check_same_thread":False})
engine = create_engine ("sqlite:///database/instrumentos.db", connect_args={"check_same_thread":False})

Session = sessionmaker (bind=engine)
session = Session()
Base = declarative_base()