from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField, SelectField

class PersonagemForm(FlaskForm):
    """
    Formulario da criacao de personagem
    """
    nome = StringField('Nome')
    raca = StringField('Raça')
    idade = IntegerField("Idade")
    peso = DecimalField("Peso (kg)", places=3)
    altura = DecimalField("Altura (m)", places=2)
    genero = SelectField("Genero", choices={"Masculino", "Feminino", "Outro"})

    cabelo_tipo = StringField('Tipo do Cabelo')
    cabelo_cor = StringField('Cor do Cabelo')
    olhos_tipo = StringField('Tipo dos Olhos')
    olhos_cor = StringField('Cor dos Olhos')
    tom_pele = StringField('Tom de pele')
    roupa_torso = StringField('Roupa do torso')
    roupa_pernas = StringField('Roupa para pernas')
    acessorios = StringField('Acessórios')
    
    travar_nome = BooleanField("Travar nome")
    travar_raca = BooleanField("Travar raca")
    travar_idade = BooleanField("Travar idade")
    travar_peso = BooleanField("Travar peso")
    travar_altura = BooleanField("Travar altura")

