from typing import List
from flask import Flask, render_template
import datetime
TEMPLATES = './templates'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route('/')
def helloworld():
    return 'Olá mundo!'

@app.route('/index')
def index():
    data = datetime.datetime.now()
    nome= 'Jaqueline'
    Lista=['https://www.youtube.com/embed/3fP541Qhfd0','https://www.youtube.com/embed/CTIs_RSPr84']
    return render_template('index.html', nome=nome, Lista=Lista, dataAtual = data)

#app.run(host='0.0.0.0', port=5000) 
    
