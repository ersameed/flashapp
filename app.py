from flask import Flask

app = Flask(__name__)


@app.route('/')
def counter():
    return 'visiters count is 0'
