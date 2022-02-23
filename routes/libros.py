from flask import Blueprint, render_template

libros = Blueprint('libros', __name__)


@libros.route('/libros')
def consultar_libros():
    return render_template('libros.html')
