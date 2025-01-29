from flask_wtf import FlaskForm
from wtforms import *

class PersonagemForm(FlaskForm):
    """
    Formulario da criacao de personagem
    """
    nome = StringField('Nome')
    raca = StringField('Raça')
    idade = IntegerField("Idade")
    peso = DecimalField("Peso (kg)", places=3)
    altura = DecimalField("Altura (m)", places=2)

    cabelo_tipo = StringField('Tipo do Cabelo')
    cabelo_cor = StringField('Cor do Cabelo')
    olhos_tipo = StringField('Tipo dos Olhos')
    olhos_cor = StringField('Cor dos Olhos')
    tom_pele = StringField('Tom de pele')
    roupa_torso = StringField('Roupa do torso')
    roupa_pernas = StringField('Roupa para pernas')
    acessorios = StringField('Acessórios')

