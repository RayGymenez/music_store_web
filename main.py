from flask import Flask, render_template
from routes.discos import discos
from routes.libros import libros
from routes.instrumentos import instrumentos
from models import Libro
import db

UPLOAD_FOLDER = './static/img/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 3 * 1000 * 1000


app.register_blueprint(discos)
app.register_blueprint(libros)
app.register_blueprint(instrumentos)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carrito')
def carrito():
    libros = db.session.query(Libro).all()
    for libro in libros:
        print(libro)
    return render_template('carrito.html',todos_los_libros=libros)


