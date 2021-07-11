from flask import Flask
import flask

TEMPLATE = './template'
STATIC = './static'
app = flask(__name__, template_folder = TEMPLATE, static_folder = STATIC)
@app.route('/')
def index():
    return 'Ola mundo'
app.run(host = "0.0.0.0", port = 5000)