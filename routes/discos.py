import os
import db
from crypt import methods
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import Disco
from werkzeug.utils import secure_filename

discos = Blueprint('discos', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


carrito = []


@discos.route('/discos')
def consultar_discos():
    discos = db.session.query(Disco).all()
    for disco in discos:
        print(disco)
    return render_template('discos.html', todos_los_discos=discos)


@discos.route("/discos/agregar", methods=['GET', 'POST'])
def agregar(args):
    carrito.append(args)
    print(carrito)
    return redirect(url_for('discos.html'))


@discos.route('/discos/crear-disco', methods=['GET', 'POST'])
def crear_discos():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return render_template('crear-disco.html')
    # '''
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form method=post enctype=multipart/form-data>
    #   <input type=file name=file>
    #   <input type=submit value=Upload>
    # </form>
    # '''
