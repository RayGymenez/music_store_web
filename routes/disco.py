from flask import Blueprint, render_template
import db
from models import Disco

discos = Blueprint('discos', __name__)


@discos.route('/discos')
def consultar_discos():
    discos = db.session.query(Disco).all()
    for disco in discos:
        print(disco)
    return render_template('discos.html', todos_los_discos=discos)


@discos.route('/crear_disco')
def crear_discos():
    disco = Disco()
