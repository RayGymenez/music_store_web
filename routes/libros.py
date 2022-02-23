import db
from flask import Blueprint, render_template
from models import Libro
libros = Blueprint('libros', __name__)


@libros.route('/libros')
def consultar_libros():
    libros = db.session.query(Libro).all()
    for libro in libros:
        print(libro)
    return render_template('libros.html', todos_los_libros=libros)
