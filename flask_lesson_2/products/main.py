from flask import Blueprint, render_template, request, redirect, session
from werkzeug.utils import secure_filename
from .utils import get_data_products, add_data_products
from .form import Add_product
import os

product = Blueprint('product', __name__, template_folder="templates")

@product.route('/products', methods=["GET"])
def get_all_products():
    data_products = get_data_products()
    products = []
    args = {}
    if request.args:
        for param in request.args:
            args['name'] = param
            args['val'] = request.args.get(param)
            products = [i for i in data_products if str(i[param]) == str(request.args.get(param))]
    else:
        products = data_products
    return render_template("all_products.html", products=products, args=args)

@product.route('/product/<id>', methods=["GET"])
def get_product(id):
    product = {}
    for data_products in get_data_products():
        if int(data_products['id']) == int(id):
            product = data_products
            break
    if session.get('product_'+str(product['id'])):
        return redirect('/products')
    sess = 'product_'+str(product['id'])
    session[sess] = True
    return render_template("product.html", product=product)

@product.route('/add_product', methods=["GET"])
def add_product_form():
    form = Add_product()
    return render_template("add_product.html", form=form)

@product.route('/add_product', methods=["POST"])
def add_product_save():
    form = Add_product(request.form)
    if form.validate():
        products=get_data_products()
        id = 1
        if len(products) > 0:
            id = products[-1]['id'] + 1
        img_name = ''
        if request.files['image']:
            image = request.files['image']
            img_name = secure_filename(image.filename)
            path = os.path.join('products/static', img_name)
            image.save(path)
        data = {
            "id": id,
            "name": form.name.data,
            "description": form.description.data,
            "img_name": img_name,
            "price": form.price.data
        }
        add_data_products(data)
        return redirect('/products')
    else:
        return redirect('/add_product')
