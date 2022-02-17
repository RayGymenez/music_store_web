from flask import Flask, render_template
import db

app = Flask (__name__)

@app.route("/")
def home():
    todos_los_discos = db.session.query(Disco).all()
    for i in todos_los_discos:
        print(i)
    return render_template("index.html")

@app.route("/crear_disco",method=["POST"])
    def crear():
        disco = Disco(titulo = request.form["titulo"], artista = request.form["artista"])
        db.session.add(disco)
        db.session.commit()
        db.session.close()
        return redirect(url_for(home))






if __name__ == ("__main__"):
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)

