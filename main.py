from flask import Flask, render_template
import db

app = Flask (__name__)

@app.route("/")
def home():
    return render_template("index.html")



if __name__ == ("__main__"):
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)

