from flask import Flask, render_template, request, send_file, make_response, session
from flask_wtf.csrf import CSRFProtect
from forms.personagem_form import PersonagemForm
from forms.fichas.grimorio_do_coracao_form import FichaGrimorioDoCoracao
from models.personagem_model import criarpersonagem
import json
from io import BytesIO
import tempfile
import os
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "61aecb89-f2b8-46b9-a85a-c05db0dd2e06"
app.config['WTF_CSRF_TIME_LIMIT'] = None

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
    
    path = request.cookies.get("ficha_gdc", "")
    path_importar = path
    if form.btn_importar.data or form.btn_salvar.data or form.btn_limpar.data:
        path_importar = ""

    if path_importar != "":
        if os.path.exists(path_importar):
            with open(path_importar, "r") as f:
                dados = json.load(f)
                form = FichaGrimorioDoCoracao(data=dados, formdata=None)

        

    if form.is_submitted():
        if (form.btn_salvar.data):
            file = json.dumps(form.to_dict(), indent=4)
            
            buffer = BytesIO(file.encode('utf-8'))
            buffer.seek(0)
            response = make_response(send_file(buffer, as_attachment=True, download_name="ficha_gdc.pk"))

            with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix="ficha_gdc.pk") as f:
                f.write(file)
                f.close()
                response.set_cookie("ficha_gdc", f.name)

            if path != "" and os.path.exists(path=path):
                os.remove(path=path)

            return response
        
        if (form.btn_importar.data):
            if form.file_importar.data:
                file = json.load(form.file_importar.data)
                form = FichaGrimorioDoCoracao(formdata=None, data=file)
        
        if (form.btn_limpar.data):
            form = FichaGrimorioDoCoracao(formdata=None, data=None)
            if path != "" and os.path.exists(path=path):
                os.remove(path=path)

    return render_template("/views/fichas/grimorio_do_coracao.html", form=form)

if __name__ == "__main__":
    app.run()