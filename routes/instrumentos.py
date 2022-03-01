import db
from flask import Blueprint, render_template
from models import Instrumentos
instrumentos = Blueprint("instrumentos", __name__)


@instrumentos.route("/instrumentos")
def consultar_instrumentos():
    instrumentos = db.session.query(Instrumentos).all()
    for instrumento in instrumentos:
        print(instrumentos)
    return render_template("instrumentos.html", todos_los_instrumentos=instrumentos)
