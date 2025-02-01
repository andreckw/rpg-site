from scripts.forms import PersonagemForm
import random
from faker import Faker
from webcolors import names


class Personagem:
    nome = ""
    raca = ""
    genero = ""
    idade = 0
    peso = 0.0
    altura = 0.0

    cabelo_tipo = ""
    cabelo_cor = ""
    olhos_formato = ""
    olhos_cor = ""
    tom_pele = ""
    

def criarpersonagem(form: PersonagemForm):
    """
        Cria um personagem
        form: Recebe um formulario de personagem para criar o personagem
        
        return classe Personagem
    """

    # Integer/Float == None
    # Str == ""
    nome = form.nome.data
    raca = form.raca.data
    genero = form.genero.data
    idade = form.idade.data
    peso = form.peso.data
    altura = form.altura.data
    tom_pele = form.tom_pele.data
    cabelo_tipo = form.cabelo_tipo.data
    cabelo_cor = form.cabelo_cor.data
    olhos_tipo = form.olhos_formato.data
    olhos_cor = form.olhos_cor.data
    
    # Gera Genero
    if form.travar_genero.data == False:
        genero = random.choice(form.genero.choices)

    # Gera nome
    if nome == "" or form.travar_nome.data == False:
        nome = geracao_nome(genero)
    
    # Gera Idade
    if idade == None or form.travar_idade.data == False:
        idade = int(random.randint(16, 40))
    
    # Gera Altura
    if altura == None or form.travar_altura.data == False:
        m = float(random.randrange(1, 2))
        cm = random.randrange(0, 100) / 100
        altura = m + cm
    
    # Gera Peso
    if peso == None or form.travar_peso.data == False:
        peso = 21.7 * (float(altura) * float(altura))
    
    # Gera Raça
    if raca == "" or form.travar_raca.data == False:
        raca = geracao_raca(altura)

    # Gera Tipo de Olho
    if form.travar_tipo_olhos.data == False:
        olhos_tipo = random.choice(form.olhos_formato.choices)
    
    # Gera Tipo de Cabelo
    if form.travar_tipo_cabelo.data == False:
        cabelo_tipo = random.choice(form.cabelo_tipo.choices)
    
    # Gera Tom de pele
    if form.travar_tom_pele.data == False:
        tom_pele = random.choice(form.tom_pele.choices)

    # Gera Cor de Cabelo
    if cabelo_cor == "" or form.travar_cor_cabelo.data == False:
        cabelo_cor = random.choice(names()).title()
    
    # Gera Cor de olhos
    if olhos_cor == "" or form.travar_cor_olhos.data == False:
        olhos_cor = random.choice(names()).title()
    
    
    new_persoangem = Personagem()
    new_persoangem.nome = nome
    new_persoangem.raca = raca
    new_persoangem.genero = genero
    new_persoangem.idade = idade
    new_persoangem.altura = round(altura, 2)
    new_persoangem.tom_pele = tom_pele
    new_persoangem.peso = round(peso, 2)
    new_persoangem.cabelo_cor = cabelo_cor
    new_persoangem.cabelo_tipo = cabelo_tipo
    new_persoangem.olhos_cor = olhos_cor
    new_persoangem.olhos_formato = olhos_tipo
        
    return new_persoangem


def geracao_nome(gender):
    
    fk = Faker(["en", "es", "PT_BR"])
    
    primeiro_nome = fk.first_name()

    if gender.lower() == "masculino":
        primeiro_nome = fk.first_name_male()
    elif gender.lower() == "feminino":
        primeiro_nome = fk.first_name_female()
    
    qtd_silabas = random.randint(3, 5)
    silabas = [
        "ba", "be", "bi", "bo", "bu", "ca", "ce", "ci", "co", "cu", "da", "de", "di", "do", "du",
        "fa", "fe", "fi", "fo", "fu", "ga", "ge", "gi", "go", "gu", "ja", "je", "ji", "jo", "ju",
        "ka", "ke", "ki", "ko", "ku", "la", "le", "li", "lo", "lu", "ma", "me", "mi", "mo", "mu", 
        "na", "ne", "ni", "no", "nu", "pa", "pe", "pi", "po", "pu", "que", "qui", "ra", "re", "ri",
        "ro", "ru", "sa", "se", "si", "so", "su", "ta", "te", "ti", "to", "tu", "va", "ve", "vi",
        "vo", "vu", "xa", "xe", "xi", "xo", "xu", "za", "ze", "zi", "zo", "zu", "bra", "bre", "bri",
        "bro", "bru", "cra", "cre", "cri", "cro", "cru", "dra", "dre", "dri", "dro", "dru", "fra", 
        "fre", "fri", "fro", "fru", "gra", "gre", "gri", "gro", "gru", "pra", "pre", "pri", "pro", 
        "pru","tra", "tre", "tri", "tro", "tru", "vra", "vre", "vri", "vro", "vru"
    ]
    
    ultimo_nome = "".join(random.choices(silabas, k=qtd_silabas)).title()
    
    return f"{primeiro_nome} {ultimo_nome}"    


def geracao_raca(altura):
    
    racas_ori = {
        "Humano": (1.5, 2.0),
        "Elfo": (1.5, 2.0),
        "Kemono": (1.5, 2.0),
        "Anões": (1.2, 1.45),
        "Fadas": (1.0, 1.3),
        "Gnomo": (1.0, 1.3),
        "Anjo": (1.0, 2.0),
        "Demonio": (1.0, 2.0),
    }
    
    racas = []
    
    for k, r in racas_ori.items():

        if altura >= r[0] and altura <= r[1]:
            racas.append(k)
    
    return f"{random.choice(racas)}"
