from flask_wtf import FlaskForm
from wtforms import FileField
import base64

class FichaForm(FlaskForm):

    def to_dict(self):
        dados = {}
        for k, v in self.data.items():
            dados[k] = v
        return dados

