from scripts.forms import PersonagemForm

def criarpersonagem(form: PersonagemForm):
    """
        Cria um personagem
        form: Recebe um formulario de personagem para criar o personagem
    """

    # Integer/Float == None
    # Str == ""
    print(form.peso.data)
    if form.peso.data == None:
        print("SIM")