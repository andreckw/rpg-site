from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField, SelectField, SelectMultipleField, FloatField, DateField, TextAreaField, FieldList, FormField, SubmitField, FileField


class PersonagemForm(FlaskForm):
    """
    Formulario da criacao de personagem
    """
    nome = StringField('Nome')
    raca = StringField('Raça')
    idade = IntegerField("Idade")
    peso = DecimalField("Peso (kg)", places=3)
    altura = DecimalField("Altura (m)", places=2)
    genero = SelectField("Genero", choices=["Masculino", "Feminino", "Outro"])

    cabelo_tipo = SelectField("Tipo de Cabelo", 
                              choices=["Liso", "Ondulado", "Cacheado", "Crespo"])
    cabelo_cor = StringField('Cor do Cabelo')
    olhos_formato = SelectField('Formato dos Olhos', 
                                choices=["Almendoados", "Arrendondados", "Felpudos", "Monólidos", "Gatinho"])
    olhos_cor = StringField('Cor dos Olhos')
    tom_pele = SelectField('Tom de pele', 
                           choices=["Albino", "Clara", "Média-clara", "Morena",
                                    "Morena-escura", "Escura"])
    
    travar_nome = BooleanField("Travar nome")
    travar_raca = BooleanField("Travar raca")
    travar_genero = BooleanField("Travar genero")
    travar_idade = BooleanField("Travar idade")
    travar_peso = BooleanField("Travar peso")
    travar_altura = BooleanField("Travar altura")
    travar_tom_pele = BooleanField("Travar Tom de Pele")
    travar_tipo_cabelo = BooleanField("Travar Formato de Cabelo")
    travar_cor_cabelo = BooleanField("Travar Cor do Cabelo")
    travar_tipo_olhos = BooleanField("Travar Tipo do Olhos")
    travar_cor_olhos = BooleanField("Travar Cor do Olhos")

