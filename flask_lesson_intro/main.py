from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())

@app.route('/author')
def get_author_page():
    return render_template("author.html")

@app.route('/<string>')
def get_item_page(string):
    data = [i for i in get_data() if string == i['title'].replace(' ', '_')]
    img = string
    if not data:
        data = [{'title': '404', 'text': 'Not found'}]
        img = '404'
        count = 0
    else:
        img = string
        count = len(data[0]['text'].split())
    return render_template("item.html", data=data, img=img, count=count)

if __name__ == "__main__":
    app.run(debug=True)
