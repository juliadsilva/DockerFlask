from app import app
from flask import render_template

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/nome')
def nome():
   return render_template('nome.html')

@app.route('/matricula')
def matricula():
   return render_template('matricula.html')

@app.route('/musica')
def musica():
   return render_template('musica.html')