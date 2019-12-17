from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/vegetables')
def vegetables():
    return render_template("vegetables.html", catalog=['beans', 'carrot', 'beetroot', 'cucumber'])

@app.route('/fruits')
def fruits():
    return render_template("fruits.html", catalog=['melon', 'apple', 'strawberry', 'grape'])

if __name__ == "__main__":
    app.run(debug=True)
