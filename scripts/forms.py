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


class CaculadoraSombrasDasAlmas(FlaskForm):
    forca = IntegerField("FOR", default=2)
    destreza = IntegerField("DES", default=2)
    saude = IntegerField("SAU", default=2)
    conhecimento = IntegerField("CON", default=2)
    comunicacao = IntegerField("COM", default=2)
    percepcao = IntegerField("PER", default=2)
    mente = IntegerField("MEN", default=2)
    
    estilo_combate = SelectField("Estilo de Combate", choices=[('punho_forte', 'Punho Forte'),
                                                               ('mente_sagaz', 'Mente Sagaz'),
                                                               ('pernas_ageis', 'Pernas Ageis'),
                                                               ('peito_diamente', 'Peito de Diamante'),
                                                               ('combate_especializado', 'Combate Especializado'),
                                                               ('ser_silencio', 'Ser do Silêncio'),
                                                               ('presenca_imponente', 'Presença Imponente'),
                                                               ('coracao_curativo', 'Coração Curativo'),
                                                               ('lider_esperanca', 'Lider Esperança')])
    
    nivel_inicial = IntegerField("Nivel inicial", default=1)
    nivel_final = IntegerField("Nivel final", default=1)
    
    auto_pontos_restantes = BooleanField("Auto adicionar pontos")

    
