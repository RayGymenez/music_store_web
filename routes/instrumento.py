from flask import Blueprint, render_template
import db
from models import Instrumento

discos = Blueprint('instrumentos', __name__)


@discos.route('/instrumentos')
def consultar_discos():
    # instrumentos = db.session.query(Instrumento).all()
    # for instrumento in instrumentos:
    #     print(instrumento)
    return render_template('instrumentos.html')
