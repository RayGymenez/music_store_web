from sqlalchemy import Column, Integer, String, Boolean
import db

class Disco(db.Base):
    _tablename_ = "disco"
    id = Column(Integer, primay_key = True)
    titulo = Column(String(200),nullable = False)
    artista = Column(String(200),nullable= False)

    def __init__ (self,titulo, artista):
        self.titulo= titulo
        self.artista= artista
        def __str__(self):
            return "disco: {} por {} ".format(self.titulo,self.artista)
