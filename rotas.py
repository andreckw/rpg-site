from flask import Flask, render_template, request, send_file
from flask_wtf.csrf import CSRFProtect
from scripts.forms import PersonagemForm, CaculadoraSombrasDasAlmas, FichaSombrasDasAlmas
from scripts.calculadora import SombraDasAlmas
from scripts.personagem import criarpersonagem
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

    return render_template("/sites/index.html")


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

    return render_template("/sites/personagem.html", form=form, new_personagem=new_personagem)


@app.route("/calculadora/sombrasdasalmas", methods=['GET', 'POST'])
def calculadora_sombras_das_almas():
    form = CaculadoraSombrasDasAlmas()
    calculadora = None

    if form.validate_on_submit():
        calculadora = SombraDasAlmas()
        calculadora = calculadora.calcular(form)
    
    
    return render_template("/sites/calculadoras/sombras_das_almas.html", form=form, calculadora=calculadora)


@app.route("/fichas/sombrasdasalmas", methods=['GET', 'POST'])
def ficha_sombras_das_almas():
    form = FichaSombrasDasAlmas()
    
    if os.path.isfile("personagem.pkl"):
        os.remove("personagem.pkl")
    
    if form.exportar.data == True:
        with tempfile.NamedTemporaryFile(mode="w",delete=False, suffix=".json") as f:
            dados_export = {}
            
            for k, v in form.data.items():
                if isinstance(v, (datetime.date, datetime.datetime)):
                  dados_export[k] = v.isoformat()
                elif k != "arquivo" and k != "importar" and k != "csrf_token" and k != "exportar":
                    dados_export[k] = v

            json.dump(dados_export, f, ensure_ascii=False)

            caminho = f.name
            
        nome = "personagem.json"
    
        if form.nome.data:
            nome = form.nome.data+".json"
            
        return send_file(caminho, as_attachment=True, download_name=nome)
    
    if form.importar.data == True:
        a = form.arquivo.data;
        
        filename = a.filename.split(".")
        
        if "json" in filename:
            dados = json.load(a.stream)
            
            for k, v in dados.items():
                if k == "data_nascimento":
                    dados[k] = datetime.date.fromisoformat(v)
            
            form = FichaSombrasDasAlmas(formdata=None, data=dados)
    
    
    return render_template("/sites/fichas/sombras_das_almas.html", form=form)

if __name__ == "__main__":
    app.run()