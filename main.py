from crypt import methods
from flask import Flask, render_template, request, session, redirect, url_for
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
app.secret_key = b'_5#/54?L"F4Q8z\n\xec]/'

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
        product_cover = request.form.get('cover')

        if product_id and product_name and product_price and request.method == 'POST':
            CartProducts = {product_id: {
                'name': product_name, 'price': product_price, 'cover': product_cover}}

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
    if 'CartProducts' in session:
        productos_carrito = session['CartProducts']
        print(productos_carrito)
        for producto_id, item in productos_carrito.items():
            print(producto_id, float(item['price']))
    else:
        productos_carrito = False

    return render_template('carrito.html', todos_los_productos=productos_carrito)


@app.route('/vaciar_carrito')
def vaciar_carrito():
    # remove the username from the session if it's there
    session.pop('CartProducts', None)
    return redirect(url_for('home'))

@app.route('/eliminar_producto',methods=["POST"])
def eliminar_producto():

    product_id = request.form.get('id')


    del session['CartProducts'][product_id]
    productos_carrito = session['CartProducts']

    session.pop('CartProducts', None)
    print("producto eliminado")

    session['CartProducts'] = productos_carrito
    return redirect(request.referrer)

