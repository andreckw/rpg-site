from flask_wtf import FlaskForm

class FichaForm(FlaskForm):

    def to_dict(self):
        dados = {}
        for k, v in self.data.items():
            dados[k] = v
        return dados
