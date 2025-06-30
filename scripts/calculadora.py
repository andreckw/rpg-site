from scripts.forms import CaculadoraSombrasDasAlmas
import random
    

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
    niveis = []
    nivel_atual = 0
    saude_nivel = []
    mente_nivel = []
    
    pv = 0
    pb = 0
    pa = 0
    aa = 0
    
    ponto_habilidade = 0
    ponto_maestria = 0
    
    pontos_restantes = 0
    
    vantagens = []
    desvantagens = []
    vantagem_talento = ""
    desvantagem_talento = ""
    pouco_folego = False
    
    def __init__(self):
        self.forca = 2
        self.destreza = 2
        self.saude = 2
        self.conhecimento = 2
        self.comunicacao = 2
        self.percepcao = 2
        self.mente = 2
        self.estilo_combate = {
            'vitalidade': [],
            'energia': [],
        }
        self.niveis = []
        self.atr_niveis = []
        
        self.pv = 75
        self.pb = 0
        self.pa = 65
        self.aa = 0
        
        self.ponto_habilidade = 0
        self.ponto_maestria = 0
        
        self.pontos_restantes = 0
        
        self.vantagens = []
        self.desvantagens = []
        self.pouco_folego = False
    
    def calcular(self, form: CaculadoraSombrasDasAlmas):
        self.niveis = []

        self.forca = form.forca.data
        self.destreza = form.destreza.data
        self.saude = form.saude.data
        self.conhecimento = form.conhecimento.data
        self.comunicacao = form.comunicacao.data
        self.percepcao = form.percepcao.data
        self.mente = form.mente.data
        self.vantagens = form.vantagens.data
        self.desvantagens = form.desvantagens.data
        self.vantagem_talento = form.vantagem_talento.data
        self.desvantagem_talento = form.desvantagem_talento.data
        
        # Calcula os pontos necessarios para o nivel inicial selecionado
        pontos_atr_necessario = 39
        i = 1
        while i <= form.nivel_inicial.data:
            if i >= 2 and i <= 5:
                pontos_atr_necessario += 1
            elif i >= 6 and i <= 10:
                pontos_atr_necessario += 2
            elif i >= 11 and i <= 20:
                pontos_atr_necessario += 3
            elif i >= 21 and i <= 40:
                pontos_atr_necessario += 4
            elif i >= 41 and i <= 50:
                pontos_atr_necessario += 5
            
            if not i % 2 == 0 and i != 1:
                pontos_atr_necessario += 7
            
            i+=1
        # Calcula o total de pontos adicionado
        total_atr = self.forca + self.destreza + self.saude + self.conhecimento + self.comunicacao + self.percepcao + self.mente
                
        self.gerar_estilo_combate(form.estilo_combate.data)
        pontos_atr_necessario += self.gerar_aura(form.aura.data)
        
        
        if form.nivel_inicial.data > form.nivel_final.data:
            form.form_errors.append("Nivel inicial MAIOR que o nivel final")
            return None
        
        # Calcula os pontos total para o nivel final selecionado
        i = form.nivel_inicial.data
        self.pv = form.pv.data
        self.pa = form.pa.data
        while i <= form.nivel_final.data:
            self.niveis.append(i)
            
            if i > form.nivel_inicial.data:
                if i >= 2 and i <= 5:
                    self.pontos_restantes += 1
                elif i >= 6 and i <= 10:
                    self.pontos_restantes += 2
                elif i >= 11 and i <= 20:
                    self.pontos_restantes += 3
                elif i >= 21 and i <= 40:
                    self.pontos_restantes += 4
                elif i >= 41 and i <= 50:
                    self.pontos_restantes += 5
                
            if i > form.nivel_inicial.data and not i % 2 == 0:
                self.forca += 1
                self.destreza += 1
                self.saude += 1
                self.conhecimento += 1
                self.comunicacao += 1
                self.percepcao += 1
                self.mente += 1
            
            self.saude_nivel.append(self.saude)
            self.mente_nivel.append(self.mente)
            i+=1
        
        self.nivel_atual = self.niveis[-1]
        self.calcular_vantagens()
        self.calcular_desvantagens()
        
        if form.auto_pontos_restantes.data == True:
            self.colocar_atributos_restantes()
        
        self.saude_nivel[-1] = self.saude
        self.mente_nivel[-1] = self.mente
        
        self.gerar_pa()
        self.gerar_pv()
        self.gerar_pb()
        self.gerar_aa()
        
        self.calcular_pontos_maetrias()
        self.calcular_pontos_habilidades()
        
        if total_atr < pontos_atr_necessario:
            form.form_errors.append(f"Pontos totais necessários não alcançado, precisa de {pontos_atr_necessario}, falta {pontos_atr_necessario - total_atr}")
            
            return None

        elif total_atr > pontos_atr_necessario and self.nivel_atual == 1:
           form.form_errors.append(f"Pontos totais acima do necessário, precisa de {pontos_atr_necessario}, precisa de -{total_atr - pontos_atr_necessario}")
            
           return None

        return self

    def colocar_atributos_restantes(self):
        
        i = 0
        while self.pontos_restantes > 0:
            pontos = random.randrange(0, self.pontos_restantes + 1)
            self.pontos_restantes -= pontos
            match (i):
                case 1: self.forca += pontos
                case 2: self.destreza += pontos
                case 3: self.saude += pontos
                case 4: self.conhecimento += pontos
                case 5: self.comunicacao += pontos
                case 6: self.percepcao += pontos
                case 7:
                    self.mente += pontos
                    i = 0
            i+=1
        
        return

    def gerar_pv(self):
        for n in self.niveis:
            
            for v in self.estilo_combate["vitalidade"]:
                print(v)
                if n >= v["n_inicio"] and n <= v["n_final"]:
                    self.pv += v["valor"] + self.saude_nivel[n - 1]
                    break


    def gerar_pa(self):
        for n in self.niveis:
            
            for m in self.estilo_combate["energia"]:
                if n >= m["n_inicio"] and n <= m["n_final"]:
                    self.pa += m["valor"] + self.mente_nivel[n - 1]
                    if n == 1 and self.pouco_folego:
                        self.pa -= (self.pa * 0.25)
                    break
    
    
    def gerar_pb(self):
        divisor = 10
        
        for n in self.niveis:
            if n % 5 == 0:
                divisor-=1

            self.pb += (self.forca + self.percepcao + self.mente) / divisor + (n * 2)

        self.pb = round(self.pb, 2)


    def gerar_aa(self):
        self.aa += (self.forca + self.destreza + self.saude + self.conhecimento + self.mente) / 3
        
        for n in self.niveis:
            if not n % 2 == 0 and n != 1:
                self.aa += 1
        
        self.aa = round(self.aa, 2)
    
    
    def calcular_pontos_maetrias(self):
        
        for n in self.niveis:
            if n % 4 == 0 and n != 1:
                self.ponto_maestria+=1


    def calcular_pontos_habilidades(self):
        
        for n in self.niveis:
            if not n % 2 == 0 and n != 1:
                self.ponto_habilidade+=1
    
    
    def gerar_aura(self, aura_form):
        
        if aura_form == "red":
            self.forca += 1
            self.mente += 1
        elif aura_form == "blue":
            self.destreza += 1
            self.conhecimento += 1
        elif aura_form == "flavus":
            self.forca += 1
            self.destreza += 1
        elif aura_form == "aureum":
            self.percepcao += 1
            self.conhecimento += 1
        elif aura_form == "purpura":
            self.comunicacao += 1
            self.mente += 1
        elif aura_form == "viridis":
            self.saude += 1
            self.mente += 1
        elif aura_form == "gray":
            return 2
        elif aura_form == "niger":
            self.mente += 1
            self.comunicacao += 1
            self.conhecimento += 1
        elif aura_form == "alba":
            self.mente += 1
            self.saude += 1
            self.conhecimento += 1
        return 0
        

    def gerar_estilo_combate(self, estilo_form):
        niveis = [(1, 1), (2, 10), (11, 20), (21, 30), (31, 40), (41, 50)]

        if estilo_form == "punho_forte":
            vitalidade = [20, 15, 25, 35, 45, 50]
            energia = [20, 15, 25, 35, 45, 50]
            if (self.nivel_atual == 1):
                self.forca += 2
        elif estilo_form == "mente_sagaz":
            vitalidade = [0, 8, 13, 18, 23, 25]
            energia = [40, 22, 37, 52, 67, 75]
            if (self.nivel_atual == 1):
                self.mente += 2
        elif estilo_form == "pernas_ageis":
            vitalidade = [25, 18, 31, 43, 56, 62]
            energia = [15, 12, 19, 27, 34, 38]
            if (self.nivel_atual == 1):
                self.destreza += 2
        elif estilo_form == "peito_diamante":
            vitalidade = [40, 22, 37, 52, 67, 75]
            energia = [0, 8, 13, 18, 23, 25]
            if (self.nivel_atual == 1):
                self.saude += 2
        elif estilo_form == "combate_especializado":
            vitalidade = [15, 12, 20, 27, 34, 38]
            energia = [25, 18, 31, 43, 56, 62]
            if (self.nivel_atual == 1):
                self.forca += 1
                self.destreza += 1
        elif estilo_form == "ser_silencio":
            vitalidade = [25, 15, 25, 35, 45, 50]
            energia = [25, 15, 25, 35, 45, 50]
            if (self.nivel_atual == 1):
                self.destreza += 1
                self.percepcao += 1
        elif estilo_form == "presenca_imponente":
            vitalidade = [30, 18, 30, 42, 54, 60]
            energia = [20, 12, 20, 28, 36, 40]
            if (self.nivel_atual == 1):
                self.comunicacao += 2
        elif estilo_form == "coracao_curativo":
            vitalidade = [10, 8, 13, 18, 23, 25]
            energia = [30, 22, 37, 52, 67, 75]
            if (self.nivel_atual == 1):
                self.conhecimento += 1
                self.mente += 1
        else:
            vitalidade = [30, 22, 37, 52, 67, 75]
            energia = [10, 8, 13, 18, 23, 25]
            if (self.nivel_atual == 1):
                self.comunicacao += 1
                self.mente += 1
            
        
        j = 0
        self.estilo_combate['vitalidade'] = []
        self.estilo_combate['energia'] = []
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
       
            
    def calcular_vantagens(self):
        
        for v in self.vantagens:
            if v == "litros_sangue":
                self.pv += 15
                
                n_final = self.nivel_atual
                
                while n_final > 1:
                    self.pv += 5
                    n_final -= 1
                    
            elif v == "incansavel":
                self.pa += 15
                
                n_final = self.nivel_atual
                
                while n_final > 1:
                    self.pa += 5
                    n_final -= 1
                
            elif v == "aura_monstruosa":
                self.aa += 2
            
            elif v == "membro_ember":
                self.mente += 1
                self.forca += 1
                self.saude += 1
                self.saude_nivel[len(self.saude_nivel) - 1] = self.saude
                self.mente_nivel[len(self.mente_nivel) - 1] = self.mente
            
            elif v == "talento_natural":
                if (self.nivel_atual == 1):
                    match (self.vantagem_talento):
                        case "FOR": self.forca += 2
                        case "DES": self.destreza += 2
                        case "SAU": 
                            self.saude += 2
                            self.saude_nivel[len(self.saude_nivel) - 1] = self.saude
                        case "CON": self.conhecimento += 2
                        case "COM": self.comunicacao += 2
                        case "PER": self.percepcao += 2
                        case "MEN": 
                            self.mente += 2
                            self.mente_nivel[len(self.mente_nivel) - 1] = self.mente
        
        
    def calcular_desvantagens(self):
        
        for v in self.desvantagens:
            if v == "saude_fragil":
                self.pv -= 25
            elif v == "pouco_folego":
                self.pouco_folego = True
            elif v == "sem_talento":
                if (self.nivel_atual == 1):
                    match (self.vantagem_talento):
                        case "FOR": self.forca -= 1
                        case "DES": self.destreza -= 1
                        case "SAU": self.saude -= 1
                        case "CON": self.conhecimento -= 1
                        case "COM": self.comunicacao -= 1
                        case "PER": self.percepcao -= 1
                        case "MEN": self.mente -= 1
                        