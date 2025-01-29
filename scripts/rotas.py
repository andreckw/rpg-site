from flask import *
from scripts.env import EnvVariables
from scripts.forms import *
from scripts.personagem import criarpersonagem

app = Flask(EnvVariables.nome);

app.config["SECRET_KEY"] = EnvVariables.secret_key

@app.route("/", methods=['GET'])
def index():

    return render_template("/sites/index.html")


@app.route("/personagem", methods=['GET', 'POST'])
def personagem():
    form = PersonagemForm();

    if form.validate_on_submit and request.method == 'POST':
        criarpersonagem(form)

    return render_template("/sites/personagem.html", form=form)