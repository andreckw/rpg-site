from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from scripts.forms import PersonagemForm, CaculadoraSombrasDasAlmas, FichaSombrasDasAlmas
from scripts.calculadora import SombraDasAlmas
from scripts.personagem import criarpersonagem

app = Flask(__name__)
app.config["SECRET_KEY"] = "61aecb89-f2b8-46b9-a85a-c05db0dd2e06"

csrf = CSRFProtect(app)

@app.route("/", methods=['GET'])
def index():

    return render_template("/sites/index.html")


@app.route("/personagem", methods=['GET', 'POST'])
def personagem():
    form = PersonagemForm()
    new_personagem = None
    
    if form.validate_on_submit() and request.method == 'POST':
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
        calculadora = SombraDasAlmas().calcular(form)
    
    
    return render_template("/sites/calculadoras/sombras_das_almas.html", form=form, calculadora=calculadora)


@app.route("/ficha/sombrasdasalmas", methods=['GET', 'POST'])
def ficha_sombras_das_almas():
    form = FichaSombrasDasAlmas()
    
    
    return render_template("/sites/fichas/sombra_das_almas.html", form=form)

if __name__ == "__main__":
    app.run()