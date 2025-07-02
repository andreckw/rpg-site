from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, BooleanField, SelectField, SelectMultipleField, FloatField, DateField, TextAreaField, FieldList, FormField


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
    
    pv = IntegerField("PV", default=75)
    pa = IntegerField("PA", default=65)
    
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
    

class HabilidadeForm(FlaskForm):
    nome = StringField("Nome Habilidade")
    desc = TextAreaField("Desc")
    nivel_atual = IntegerField("Nivel Atual")
    nivel_max = IntegerField("Nivel Max")
    custo_pa = FloatField("Custo PA")
    custo_aa = FloatField("Custo AA")


class ItensForm(FlaskForm):
    nome = StringField("Nome")
    desc = TextAreaField("Descricao")
    tipo = SelectField(label="Tipo", choices=["Arma", "Item"])
    


class VeDForm(FlaskForm):
    nome = StringField("Nome")
    desc = TextAreaField("Desc")
    custo = IntegerField("Custo")
    tipo = SelectField("tipo", choices=["V", "D"])
    

class MaestriasForm(FlaskForm):
    nome = StringField("Nome: ")
    atr = StringField("ATR: ")
    nivel = IntegerField("Nivel: ")
    exp = IntegerField("Exp: ")
    desc = TextAreaField("Desc: ")


class FichaSombrasDasAlmas(FlaskForm):
    nome = StringField(label="Nome")
    idade = IntegerField(label="Idade")
    data_nascimento = DateField(label="Data Nascimento")
    
    nivel = IntegerField(label="Nivel")
    jogador = StringField(label="Jogador")
    altura = FloatField(label="Altura (m)")
    sexo = SelectField(label="Sexo", choices=["Masculino", "Feminino", "Outro"])
    peso = FloatField(label="Peso (kg)")
    
    forca = IntegerField("FOR", default=2)
    destreza = IntegerField("DES", default=2)
    saude = IntegerField("SAU", default=2)
    conhecimento = IntegerField("CON", default=2)
    comunicacao = IntegerField("COM", default=2)
    percepcao = IntegerField("PER", default=2)
    mente = IntegerField("MEN", default=2)
    
    pv_atual = IntegerField("PV", default=75)
    pv_max = IntegerField("PV Max", default=75)
    pb_atual = IntegerField("PB", default=0)
    pb_max = IntegerField("PB Max", default=0)
    pa_atual = IntegerField("PA", default=65)
    pa_max = IntegerField("PA Max", default=65)
    aa_atual = IntegerField("AA", default=0)
    aa_max = IntegerField("AA Max", default=0)
    
    
    soul = TextAreaField(label="Soul: ")
    aura = TextAreaField(label="Aura: ")
    estilo_combate = SelectField("Estilo de Combate", choices=[('punho_forte', 'Punho Forte'),
                                                               ('mente_sagaz', 'Mente Sagaz'),
                                                               ('pernas_ageis', 'Pernas Ageis'),
                                                               ('peito_diamante', 'Peito de Diamante'),
                                                               ('combate_especializado', 'Combate Especializado'),
                                                               ('ser_silencio', 'Ser do Silêncio'),
                                                               ('presenca_imponente', 'Presença Imponente'),
                                                               ('coracao_curativo', 'Coração Curativo'),
                                                               ('lider_esperanca', 'Lider Esperança')])
    
    van_des = FieldList(FormField(VeDForm), min_entries=1)
    
    personalidade = TextAreaField("Personalidade: ")
    
    maestrias = FieldList(FormField(MaestriasForm), label="Maestrias", min_entries=1);
    
    aparencia = TextAreaField(label="Aparencia: ")
    historia = TextAreaField(label="Historia: ")
    
    habilidades = FieldList(FormField(HabilidadeForm), label="Habilidades", min_entries=1)
    
    inventario = FieldList(FormField(ItensForm), label="Inventario", min_entries=1)

    

