from typing import Text
from flask import Flask

TEMPLATES = './templates'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route('/')
def helloworld():
    return 'Olá, mundo!'

app.run(host='0.0.0.0', port=5000)
    
