from flask import Flask, render_template, url_for, redirect, request
import db
from models import Disco

app = Flask(__name__)



if __name__ == ("__main__"):
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
