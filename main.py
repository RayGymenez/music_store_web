from flask import Flask, render_template, url_for, redirect, request
import db
from models import Disco

app = Flask(__name__)


@app.route("/")
def home():
    #     todos_los_discos = db.session.query(Disco).all()
    #     for disco in todos_los_discos:
    #         print(disco)
    return render_template('index.html')


@app.route("/crear_disco", methods=["POST"])
def crear():
    disco = Disco(Nombre=request.form['nombre'],
                  Precio=request.form['precio'])
    db.session.add(disco)
    db.session.commit()
    db.session.close()
    return redirect(url_for(home))


if __name__ == ("__main__"):
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
