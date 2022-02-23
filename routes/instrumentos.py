from flask import Blueprint, render_template

instrumentos = Blueprint('instrumentos', __name__)


@instrumentos.route('/instrumentos')
def consultar_instrumentos():
    return render_template('instrumentos.html')
