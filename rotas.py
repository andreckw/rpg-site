from flask import Flask, render_template, request, send_file
from flask_wtf.csrf import CSRFProtect
from forms.personagem_form import PersonagemForm
from forms.ficha_grimorio_do_coracao_form import FichaGrimorioDoCoracao
from models.personagem_model import criarpersonagem
import json
import tempfile
import os
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "61aecb89-f2b8-46b9-a85a-c05db0dd2e06"

csrf = CSRFProtect(app)
csrf.init_app(app)

@app.route("/", methods=['GET'])
def index():

    return render_template("/views/index.html")


@app.route("/personagem", methods=['GET', 'POST'])
def personagem():
    form = PersonagemForm()
    new_personagem = None
    if request.method == 'POST':
        new_personagem = criarpersonagem(form)
        form.genero.data = new_personagem.genero
        form.cabelo_tipo.data = new_personagem.cabelo_tipo
        form.olhos_formato.data = new_personagem.olhos_formato
        form.tom_pele.data = new_personagem.tom_pele

    return render_template("/views/personagem.html", form=form, new_personagem=new_personagem)

@app.route("/ficha/grimoriodocoracao", methods=["GET", "POST"])
def ficha_grimorio_do_coracao():
    form = FichaGrimorioDoCoracao()

    return render_template("/views/fichas/grimorio_do_coracao.html", form=form)

if __name__ == "__main__":
    app.run()