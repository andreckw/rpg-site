from flask import Flask, render_template, request
from scripts.forms import PersonagemForm
from scripts.personagem import criarpersonagem

app = Flask(__name__)

app.config["SECRET_KEY"] = "61aecb89-f2b8-46b9-a85a-c05db0dd2e06"

@app.route("/", methods=['GET'])
def index():

    return render_template("/sites/index.html")


@app.route("/personagem", methods=['GET', 'POST'])
def personagem():
    form = PersonagemForm()
    new_personagem = None
    
    if form.validate_on_submit and request.method == 'POST':
        new_personagem = criarpersonagem(form)
        form.genero.data = new_personagem.genero
        form.cabelo_tipo.data = new_personagem.cabelo_tipo
        form.olhos_formato.data = new_personagem.olhos_formato
        form.tom_pele.data = new_personagem.tom_pele

    return render_template("/sites/personagem.html", form=form, new_personagem=new_personagem)

if __name__ == "__main__":
    app.run()