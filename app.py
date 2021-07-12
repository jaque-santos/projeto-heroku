from flask import Flask, render_template
TEMPLATES = './templates'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route('/')
def helloworld():
    return 'Olá mundo!'

@app.route('/index')
def index():
    nome= 'Jaqueline'
    return render_template('index.html', nome=nome)
app.run(host='0.0.0.0', port=5000) 
    
