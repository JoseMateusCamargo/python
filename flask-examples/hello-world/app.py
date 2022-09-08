from flask import Flask

# Documentation: https://flask.palletsprojects.com/en/2.0.x/
app = Flask(__name__)


@app.route('/')
def hello_():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True)
