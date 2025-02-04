from scripts.forms import CaculadoraSombrasDasAlmas

    

class SombraDasAlmas():
    forca = 2
    destreza = 2
    saude = 2
    conhecimento = 2
    comunicacao = 2
    percepcao = 2
    mente = 2
    estilo_combate = {
        'vitalidade': [],
        'energia': [],
    }
    
    pv = 0
    pb = 0
    pa = 0
    aa = 0
    
    def calcular(self, form: CaculadoraSombrasDasAlmas):
        self.forca = form.forca.data
        self.destreza = form.destreza.data
        self.saude = form.saude.data
        self.conhecimento = form.conhecimento.data
        self.comunicacao = form.comunicacao.data
        self.percepcao = form.percepcao.data
        self.mente = form.mente.data
        
        total = self.forca + self.destreza + self.saude + self.conhecimento + self.comunicacao + self.percepcao + self.mente
        
        if total < 39:
            form.form_errors.append('A soma dos atributos está abaixo de 39 pontos')
            return None
        
        if total > 39:
            form.form_errors.append('A soma dos atributos está acima de 39 pontos')
            return None
        
        self.gerar_estilo_combate(form.estilo_combate.data)
        
    
    def gerar_estilo_combate(self, estilo_form):
        niveis = [(1, 1), (2, 10), (11, 20), (21, 30), (31, 40), (41, 50)]
        vitalidade = [20, 15, 25, 35, 45, 50]
        energia = [20, 15, 25, 35, 45, 50]
        
        if estilo_form == "punho_forte":
            vitalidade = [20, 15, 25, 35, 45, 50]
            energia = [20, 15, 25, 35, 45, 50]
            self.destreza += 2
        
        j = 0
        for i in niveis:
            n_vitalidade = {
                "n_inicio": i[0],
                "n_final": i[1],
                "valor": vitalidade[j],
            }
            
            n_energia = {
                "n_inicio": i[0],
                "n_final": i[1],
                "valor": energia[j],
            }
            
            self.estilo_combate['vitalidade'].append(n_vitalidade)
            self.estilo_combate['energia'].append(n_energia)
            
            j+=1