# coding: utf-8
import os
from flask import Flask, render_template, json, Response
from lib.permutacao import processar

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route("/")
def home():
	return render_template('home.html')

@app.route("/<qtd_amarelas>/<qtd_vermelhas>/<qtd_azuis>/<qtd_verdes>")
def experimento(qtd_amarelas=None, qtd_vermelhas=None, qtd_azuis=None, qtd_verdes=None):
	total_bolas, total_tubos, tubos = processar(qtd_amarelas, qtd_vermelhas, qtd_azuis, qtd_verdes)
	return render_template('experimento.html', titulo=u'Título teste', qtd_amarelas=qtd_amarelas, qtd_vermelhas=qtd_vermelhas, qtd_azuis=qtd_azuis, qtd_verdes=qtd_verdes, total_bolas=total_bolas, total_tubos=total_tubos, tubos=tubos)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	if port == 5000:
		app.debug = True
	app.run(host='0.0.0.0', port=port)