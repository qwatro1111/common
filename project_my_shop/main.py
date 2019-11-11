from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'my shop'

if __name__ == "__main__":
    app.run(debug=True)
