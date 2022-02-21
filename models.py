from db import Base
from sqlalchemy import Column, Integer, Numeric, Text


class Disco(Base):
    __tablename__ = "discos"
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    artist = Column(Text, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Numeric, nullable=False)
    cover = Column(Text)

    def __init__(self, title, artist, year, price, cover=None):
        self.title = title
        self.artist = artist
        self.year = year
        self.price = price
        self.cover = cover

    def __repr__(self):
        return f"Disco {self.id}: {self.title} by {self.artist}"
