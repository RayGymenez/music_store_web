import db
from sqlalchemy import Column, Integer, Text
from tokenize import Double


class Disco(db.Base):
    __tablename__ = "Discos"
    id = Column(Integer, primary_key=True)
    Nombre = Column(Text, nullable=False)
    Precio = Column(Double, nullable=False)

    def __init__(self, nombre, precio):
        self.Nombre = nombre
        self.Precio = precio

        def __str__(self):
            return "El disco {} vale {} euros.".format(self.Nombre, self.Precio)
