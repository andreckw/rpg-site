from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField, SelectField, SelectMultipleField, FloatField


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
                                                               ('peito_diamante', 'Peito de Diamante'),
                                                               ('combate_especializado', 'Combate Especializado'),
                                                               ('ser_silencio', 'Ser do Silêncio'),
                                                               ('presenca_imponente', 'Presença Imponente'),
                                                               ('coracao_curativo', 'Coração Curativo'),
                                                               ('lider_esperanca', 'Lider Esperança')])
    
    aura = SelectField("Aura", choices=[('red', 'Red Aura'),
                                        ('blue', 'Blue Aura'),
                                        ('flavus', 'Flavus Aura'),
                                        ('aureum', 'Aureum Aura'),
                                        ('purpura', 'Purpura Aura'),
                                        ('viridis', 'Viridis Aura'),
                                        ('gray', 'Gray Aura'),
                                        ('niger', 'Niger Aura'),
                                        ('alba', 'Alba Aura')])
    
    nivel_inicial = IntegerField("Nivel inicial", default=1)
    nivel_final = IntegerField("Nivel final", default=1)
    
    auto_pontos_restantes = BooleanField("Auto adicionar pontos")
    
    vantagens = SelectMultipleField(label="Vantagens", choices=[('litros_sangue', 'Litros de Sangue'),
                                    ('incansavel', 'Incansável'),
                                    ('aura_monstruosa', "Aura Monstruosa"),
                                    ('talento_natural', 'Talento Natural'),
                                    ('membro_ember', 'Membro da Ember of Souls')])

    vantagem_talento = SelectField(label="Talento Natural", choices=["FOR", "DES", "SAU",
                                                                     "CON","COM", "PER", "MEN"])
    
    desvantagens = SelectMultipleField(label="Desvantagens", choices=[('saude_fragil', 'Saúde Frágil'),
                                                                      ('pouco_folego', "Pouco Fôlego "),
                                                                      ('sem_talento', 'Sem Talento')])
    
    desvantagem_talento = SelectField(label="Sem Talento", choices=["FOR", "DES", "SAU",
                                                                     "CON","COM", "PER", "MEN"])

    
