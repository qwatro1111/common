from flask import Blueprint, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from .utils import get_data_supermarkets, add_data_supermarkets
from .form import Add_supermarket
import os

supermarket = Blueprint(
    'supermarket',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/products/static"
)

@supermarket.route('/supermarket', methods=["GET"])
def get_all_supermarkets():
    data_supermarkets = get_data_supermarkets()
    supermarkets = []
    args = {}
    if request.args:
        for param in request.args:
            args['name'] = param
            args['val'] = request.args.get(param)
            supermarkets = [i for i in data_supermarkets if str(i[param]) == str(request.args.get(param))]
    else:
        supermarkets = data_supermarkets
    return render_template("all_supermarkets.html", supermarkets=supermarkets, args=args)

@supermarket.route('/supermarket/<id>', methods=["GET"])
def get_supermarket(id):
    supermarket = {}
    for data_supermarkets in get_data_supermarkets():
        if int(data_supermarkets['id']) == int(id):
            supermarket = data_supermarkets
            break
    if session.get('supermarket_'+str(supermarket['id'])):
        return redirect('/supermarkets')
    sess = 'supermarket_'+str(supermarket['id'])
    session[sess] = True
    return render_template("supermarket.html", supermarket=supermarket)

@supermarket.route('/add_supermarket', methods=["GET"])
def add_supermarket_form():
    form = Add_supermarket()
    return render_template("add_supermarket.html", form=form)

@supermarket.route('/add_supermarket', methods=["POST"])
def add_supermarket_save():
    form = Add_supermarket(request.form)
    if form.validate():
        supermarkets=get_data_supermarkets()
        id = 1
        if len(supermarkets) > 0:
            id = supermarkets[-1]['id'] + 1
        img_name = ''
        if request.files['image']:
            image = request.files['image']
            img_name = secure_filename(image.filename)
            path = os.path.join('supermarkets/static', img_name)
            image.save(path)
        data = {
            "id": id,
            "name": form.name.data,
            "location": form.location.data,
            "img_name": img_name,
        }
        add_data_supermarkets(data)
        return redirect('/supermarket')
    else:
        return redirect('/add_supermarket')
