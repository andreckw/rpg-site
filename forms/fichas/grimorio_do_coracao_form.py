from forms.fichas.ficha_form import FichaForm
from wtforms import StringField, IntegerField, SelectField, FieldList, FormField, TextAreaField, FloatField, FileField, BooleanField, SubmitField
import base64

def arcanas():
    return ["0 - O Tolo", "I - O Mago", "II - A Sacerdotisa", "III - A Imperatriz", "IV - O Imperado", "V - Hierofante", "VI - Os Amantes", "VII - A Carruagem", "VIII - A Justiça", "IX - O Eremita", "X - A Fortuna", "XI - A Força", "XII - O Enforcado", "XIII - A Morte", "XIV - A Temperança", "XV - O Demônio", "XVI - A Torre", "XVII - A Estrela", "XVIII - A Lua", "XIX - O Sol", "XX - Julgamento/Aeon", "XXI - O Mundo"]

def tipos():
    return ["Nenhum", "Físico", "Fogo", "Gelo", "Vento", "Raio", "Nuclear", "Psicocinese", "Luz", "Trevas", "Onipotente", "Buff", "Debuff", "Cura", "Status", "Intel"]

def afinidades():
    return ["Neutro", "Fraco", "Resiste", "Anula", "Reflete", "Drena"]

class MagiaGDC(FichaForm):
    magia = StringField(label="MAGIA")
    tipo = SelectField(choices=tipos(), label="TIPO")
    cat = StringField(label="CAT.")
    tier = StringField(label="TIER")
    alvo = StringField(label="ALVO")
    efeito = TextAreaField(label="EFEITO")
    usos = IntegerField(label="USOS")
    usos_max = IntegerField(label="USOS MAX")
    repr = IntegerField(label="REPR")


class PersonaFichaGDC(FichaForm):
    nome = StringField(label="NOME")
    arcana = SelectField(label="ARCANA", choices=arcanas())
    nivel = IntegerField(label="Nv.")
    pm = IntegerField(label="PM")

    hab_natural = TextAreaField(label="HAB. NATURAL")

    tipos = FieldList(SelectField(choices=tipos()), label="Tipos", min_entries=4, max_entries=4)
    res = FieldList(SelectField(choices=afinidades()), label="RESISTENCIAS", min_entries=11, max_entries=11)

    forca = IntegerField(label="FOR")
    tec = IntegerField(label="TEC")
    vit = IntegerField(label="VIT")
    mag = IntegerField(label="MAG")
    agi = IntegerField(label="AGI")
    sor = IntegerField(label="SOR")

    conhecimento = IntegerField(label="CONHECIMENTO")
    disciplina = IntegerField(label="DISCIPLINA")
    empatia = IntegerField(label="EMPATIA")
    charma = IntegerField(label="CHARME")
    expressao = IntegerField(label="EXPRESSÃO")
    coragem = IntegerField(label="CORAGEM")

    magias = FieldList(FormField(MagiaGDC), label="MAGIAS", min_entries=8)

    notas = TextAreaField(label="NOTAS")



class ItemForm(FichaForm):
    nome = TextAreaField(label="NOME/DESCRICAO")
    qtd = IntegerField(label="QTD")


class ConfidentsForm(FichaForm):
    nome = StringField(label="NOME")
    rank = IntegerField(label="RANK")


class PersonagemFichaGDC(FichaForm):

    retrato = FileField(label="Retrato")
    
    personagem = StringField(label="PERSONAGEM")
    exp = IntegerField(label="EXP")
    ocupacao = StringField(label="OCUPAÇÃO")
    skill = StringField(label="SKILL")
    pr = FloatField(label="PR")
    pr_bloco = FloatField(label="PR/BLOCO")
    blocos_trab = FieldList(BooleanField(), min_entries=7, max_entries=7)
    
    atq_secudario = StringField(label="ATQ.SECUNDÁRIO")
    atq_dano = StringField(label="DANO")
    atq_alc = IntegerField(label="ALC")
    atq_efe = StringField(label="EFEITO")
    
    equip_misto = TextAreaField(label="EQUIP. MISTO")

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
        return arcanas()



class FichaGrimorioDoCoracao(FichaForm):

    ficha_personagem = FormField(PersonagemFichaGDC)
    ficha_personas = FieldList(FormField(PersonaFichaGDC), label="PERSONAS", min_entries=7)
    classe = SelectField(label="CLASSE", choices=["Emergentes", "Cartas-Coringa", "Sombras", "Surpressores", "Tochas"])

    nivel = IntegerField(label="NÍVEL")
    arcana = SelectField(label="ARCANA", choices=arcanas())
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

    persona_conv = StringField(label="CONVICÇÃO")

    arma_nome = StringField(label="ARMA")
    arma_dano = StringField(label="DANO")
    arma_alc = IntegerField(label="ALC")
    arma_efe = TextAreaField(label="EFEITO")

    armadura_nome = StringField(label="ARMADURA")
    armadura_rd = StringField(label="RD")
    armadura_efe = TextAreaField(label="EFEITO")

    acessorio = StringField(label="ACESSÓRIO")
    acessorio_efe = TextAreaField(label="EFEITO")

    btn_salvar = SubmitField(label="Salvar")

    file_importar = FileField(label="Importar")
    btn_importar = SubmitField(label="Importar")

    @property
    def nomes_resistencias(self):
        return ["Fisico", "Fogo", "Gelo", "Vento", "Raio", "Nuclear", "Psicocinese", "Luz", "Trevas", "Status", "Intel"]

    def to_dict(self):
        dados = {}
        for k, v in self.data.items():
            dados[k] = v
        
        dados["ficha_personagem"]["retrato"] = base64.b64encode(self.ficha_personagem.retrato.data.read()).decode("utf-8")

        dados["file_importar"] = base64.b64encode(self.file_importar.data.read()).decode("utf-8")
        return dados

