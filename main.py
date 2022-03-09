from crypt import methods
from flask import Flask, render_template, request, session, redirect
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
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.register_blueprint(discos)
app.register_blueprint(libros)
app.register_blueprint(instrumentos)


def UnirCarrito(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/agregar_producto_carrito', methods=['POST'])
def agregar_producto_carrito():
    try:
        product_id = request.form.get('id')
        product_name = request.form.get('name')
        product_price = request.form.get('price')
        print(product_id)
        if product_id and product_name and product_price and request.method == 'POST':
            CartProducts = {product_id: {
                'name': product_name, 'price': product_price}}

            print(CartProducts)
            if 'CartProducts' in session:
                print(session['CartProducts'])
                if product_id in session['CartProducts']:
                    print('El producto ya se encuentra en el carrito')
                else:
                    session['CartProducts'] = UnirCarrito(
                        session['CartProducts'], CartProducts)
                    return redirect(request.referrer)
            else:
                session['CartProducts'] = CartProducts

    except Exception as e:
        print(e)
    finally:
        return redirect(request.referrer)


@app.route('/carrito')
def carrito():
    productos_carrito = session['CartProducts']
    print(productos_carrito)
    for producto in productos_carrito:
        print(producto)

    return render_template('carrito.html', todos_los_productos=productos_carrito)
