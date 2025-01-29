from scripts.forms import PersonagemForm
import random
from faker import Faker

class Personagem:
    nome = ""
    raca = ""
    genero = ""
    idade = 0
    peso = 0.0
    altura = 0.0

    cabelo_tipo = ""
    cabelo_cor = ""
    olhos_tipo = ""
    olhos_cor = ""
    tom_pele = ""
    roupa_torso = ""
    roupa_pernas = ""
    acessorios = ""
    
    

def criarpersonagem(form: PersonagemForm):
    """
        Cria um personagem
        form: Recebe um formulario de personagem para criar o personagem
        
        return classe Personagem
    """

    # Integer/Float == None
    # Str == ""
    nome = form.nome.data
    genero = form.genero.data
    idade = form.idade.data
    peso = form.peso.data
    altura = form.altura.data
    
    if nome == "" or form.travar_nome.data == False:
        nome = geracao_nome(genero)
    
    if idade == None or form.travar_idade.data == False:
        idade = int(random.randint(16, 40))
    
    if altura == None or form.travar_altura.data == False:
        m = float(random.randrange(1, 2))
        cm = random.randrange(0, 100) / 100
        altura = m + cm
    
    if peso == None or form.travar_peso.data == False:
        peso = 21.7 * (float(altura) * float(altura))
        
    new_persoangem = Personagem()
    new_persoangem.nome = nome
    new_persoangem.genero = genero
    new_persoangem.idade = idade
    new_persoangem.altura = altura
    new_persoangem.peso = peso
    
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
        "pru","tra", "tre", "tri", "tro", "tru"
    ]
    
    ultimo_nome = "".join(random.choices(silabas, k=qtd_silabas)).title()
    
    return f"{primeiro_nome} {ultimo_nome}"