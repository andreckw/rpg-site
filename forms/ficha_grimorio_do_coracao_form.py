from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FieldList, FormField, TextAreaField, FloatField, FileField, BooleanField

class PersonaFichaGDC(FlaskForm):
    nome = StringField(label="NOME")
    arcana = StringField(label="ARCANA")
    nivel = IntegerField(label="Nv.")

class ItemForm(FlaskForm):
    nome = TextAreaField(label="NOME/DESCRICAO")
    qtd = IntegerField(label="QTD")

class ConfidentsForm(FlaskForm):
    nome = StringField(label="NOME")
    rank = IntegerField(label="RANK")

class PersonagemFichaGDC(FlaskForm):

    retrato = FileField(label="Retrato")
    
    personagem = StringField(label="PERSONAGEM")
    exp = IntegerField(label="EXP")
    ocupacao = StringField(label="OCUPAÇÃO")
    skill = StringField(label="SKILL")
    pr = FloatField(label="PR")
    pr_bloco = FloatField(label="PR/BLOCO")
    blocos_trab = FieldList(BooleanField(), min_entries=7, max_entries=7)
    
    atq_secudario = StringField(label="ATAQUE SECUNDÁRIO")
    atq_dano = StringField(label="DANO")
    atq_alc = IntegerField(label="ALC")
    atq_efe = StringField(label="EFEITO")
    
    equip_misto = TextAreaField(label="EQUIP. MISTO")

    personas = FieldList(FormField(PersonaFichaGDC),label="PERSONAS", min_entries=7)

    itens = FieldList(FormField(ItemForm), label="ITENS", min_entries=9)

    notas = TextAreaField(label="NOTAS")

    feitos = FieldList(TextAreaField(), label="FEITOS", min_entries=12)

    confidents = FieldList(FormField(ConfidentsForm), label="CONFIDENTS", min_entries=19)

    @property
    def nome_blocos_trabalhos(self):
        return ["DOM", "SEG", "TER", "QUA", "QUI", "SEX", "SAB"]

    @property
    def nome_feitos(self):
        return ["Nv.2", "Nv.4", "Nv.6", "Nv.8", "Nv.10", "Nv.12", "Nv.14", "Nv.16", "Nv.18", "Nv.20", "Extra1", "Extra2"]
    
    @property
    def nome_confidents(self):
        return ["O Louco","O Mago","A Sacerdotisa","A Imperatriz","O Imperador","O Hierofante","Os Amantes","A Carruagem","A Justiça","O Eremita", "A Fortuna","A Força","O Enforcado","A Morte","A Temperança","O Diabo","A Torre","A Estrela","A Lua","O Sol","O Julgamento","O Mundo"]


class FichaGrimorioDoCoracao(FlaskForm):

    ficha_personagem = FormField(PersonagemFichaGDC)
    classe = StringField(label="CLASSE")
    nivel = IntegerField(label="NÍVEL")
    arcana = StringField(label="ARCANA")
    jogador = StringField(label="JOGADOR")

    forca = IntegerField(label="FORÇA (FOR)")
    tec = IntegerField(label="TÉCNICA (TEC)")
    vit = IntegerField(label="VITALIDADE (VIT)")
    mag = IntegerField(label="MAGIA (MAG)")
    agi = IntegerField(label="AGILIDADE (AGI)")
    sor = IntegerField(label="SORTE (SOR)")

    pv = IntegerField(label="PONTOS DE VIDA")
    energia = IntegerField(label="ENERGIA")
    rd = IntegerField(label="RED. DANO")
    cond = TextAreaField(label="BUFF/CONDIÇÃO")

    hab_soc_con_pts = IntegerField()
    hab_soc_con_tier = SelectField(choices=["O", "I", "II", "III", "IV", "V"])
    hab_soc_con_titulo = SelectField(choices=["Preguiçoso", "Ciente", "Sabido", "Estudado", "Enciclopédico", "Erudita"])

    hab_soc_dis_pts = IntegerField()
    hab_soc_dis_tier = SelectField(choices=["O", "I", "II", "III", "IV", "V"])
    hab_soc_dis_titulo = SelectField(choices=["Desatentos", "Decente", "Persistente", "Minucioso", "Magistral", "Transcendente"])

    hab_soc_emp_pts = IntegerField()
    hab_soc_emp_tier = SelectField(choices=["O", "I", "II", "III", "IV", "V"])
    hab_soc_emp_titulo = SelectField(choices=["Indiferentes", "Inofensivo", "Gentil", "Generoso", "Altruísta", "Angelical"])

    hab_soc_cha_pts = IntegerField()
    hab_soc_cha_tier = SelectField(choices=["O", "I", "II", "III", "IV", "V"])
    hab_soc_cha_titulo = SelectField(choices=["Sem Graça", "Existente", "Confiante", "Suave", "Popular", "Debonair"])

    hab_soc_exp_pts = IntegerField()
    hab_soc_exp_tier = SelectField(choices=["O", "I", "II", "III", "IV", "V"])
    hab_soc_exp_titulo = SelectField(choices=["Monótonos", "Rudimentar", "Eloquentes", "Inspiradora", "Tocante", "Fascinante"])

    hab_soc_cor_pts = IntegerField()
    hab_soc_cor_tier = SelectField(choices=["O", "I", "II", "III", "IV", "V"])
    hab_soc_cor_titulo = SelectField(choices=["Tímidos", "Comum", "Determinada", "Firme", "Destemidos", "Fodão"])

    pts_aspecto = IntegerField(label="PTS ASPEC.")
    aspectos = TextAreaField(label="ASPECTOS")

    persona_nome = StringField(label="NOME")
    persona_nv = IntegerField(label="Nv.")
    persona_pm = IntegerField(label="PM") #Pontos de magia
    persona_conv = StringField(label="CONVICÇÃO")
    persona_hab_natural = TextAreaField(label="HAB. NATURAL")
    persona_tipos = FieldList(StringField(), label="Tipos", min_entries=4, max_entries=4)
    persona_res = FieldList(StringField(), label="RESISTENCIAS", min_entries=11, max_entries=11)

    arma_nome = StringField(label="ARMA")
    arma_dano = StringField(label="DANO")
    arma_alc = IntegerField(label="ALC")
    arma_efe = TextAreaField(label="EFEITO")

    armadura_nome = StringField(label="ARMADURA")
    armadura_rd = StringField(label="RD")
    armadura_efe = TextAreaField(label="EFEITO")

    acessorio = StringField(label="ACESSÓRIO")
    acessorio_efe = TextAreaField(label="EFEITO")

    @property
    def nomes_resistencias(self):
        return ["Fisico", "Fogo", "Gelo", "Vento", "Raio", "Nuclear", "Psicocinese", "Luz", "Trevas", "Status", "Intel"]
