from flask import Flask, render_template
from routes.disco import discos
from routes.libro import libros

app = Flask(__name__)

app.register_blueprint(discos)
app.register_blueprint(libros)


@app.route('/')
def home():
    return render_template('index.html')

