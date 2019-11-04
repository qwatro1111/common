from flask import Flask, render_template, session, redirect
from supermarkets.main import supermarket
from products.main import product

app = Flask(__name__)
app.register_blueprint(supermarket)
app.register_blueprint(product)

app.config['SECRET_KEY'] = 'my_first_secret_key'
app.config['CSRF_ENABLED'] = True

@app.route('/')
def get_home_page():
    return render_template("home.html")

@app.route('/restart')
def restart():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
