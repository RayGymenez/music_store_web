from db import Base
from sqlalchemy import Column, Integer, Numeric, Text


class Disco(Base):
    __tablename__ = "discos"
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    artist = Column(Text, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Numeric, nullable=False)

    def __init__(self, title, artist, year, price):
        self.title = title
        self.artist = artist
        self.year = year
        self.price = price

    def __repr__(self):
        return f"Disco {self.id}: {self.title} by {self.artist}"
