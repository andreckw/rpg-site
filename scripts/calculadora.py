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
    niveis = []
    
    pv = 75
    pb = 0
    pa = 65
    aa = 0
    
    ponto_habilidade = 0
    ponto_maestria = 0
    
    def calcular(self, form: CaculadoraSombrasDasAlmas):
        self.niveis = []

        self.forca = form.forca.data
        self.destreza = form.destreza.data
        self.saude = form.saude.data
        self.conhecimento = form.conhecimento.data
        self.comunicacao = form.comunicacao.data
        self.percepcao = form.percepcao.data
        self.mente = form.mente.data
        
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

        pontos_atr_total = 39
        
        if form.nivel_inicial.data > form.nivel_final.data:
            form.form_errors.append("Nivel inicial MAIOR que o nivel final")
            return None
        
        # Calcula os pontos total para o nivel final selecionado
        i = 1
        while i <= form.nivel_final.data:
            self.niveis.append(i)
            
            if i >= 2 and i <= 5:
                pontos_atr_total += 1
            elif i >= 6 and i <= 10:
                pontos_atr_total += 2
            elif i >= 11 and i <= 20:
                pontos_atr_total += 3
            elif i >= 21 and i <= 40:
                pontos_atr_total += 4
            elif i >= 41 and i <= 50:
                pontos_atr_total += 5
                
            if i > form.nivel_inicial.data and not i % 2 == 0:
                self.forca += 1
                self.destreza += 1
                self.saude += 1
                self.conhecimento += 1
                self.comunicacao += 1
                self.percepcao += 1
                self.mente += 1
            
            i+=1        
        
        self.gerar_pa()
        self.gerar_pv()
        self.gerar_pb()
        self.gerar_aa()
        
        self.calcular_pontos_maetrias()
        self.calcular_pontos_habilidades()
        
        if total_atr < pontos_atr_necessario:
            form.form_errors.append(f"Pontos totais necessários não alcançado, precisa de {pontos_atr_necessario}, falta {pontos_atr_necessario - total_atr}")
            
            return None

        elif total_atr > pontos_atr_necessario:
            form.form_errors.append(f"Pontos totais acima do necessário, precisa de {pontos_atr_necessario}, precisa de -{total_atr - pontos_atr_necessario}")
            
            return None

        return self


    def gerar_pv(self):
        for n in self.niveis:
            
            for v in self.estilo_combate["vitalidade"]:
                if n >= v["n_inicio"] and n <= v["n_final"]:
                    self.pv += v["valor"]
                    break
        
        self.pv += self.saude


    def gerar_pa(self):
        for n in self.niveis:
            
            for m in self.estilo_combate["energia"]:
                if n >= m["n_inicio"] and n <= m["n_final"]:
                    self.pa += m["valor"]
                    break
        
        self.pa += self.mente
    
    
    def gerar_pb(self):
        divisor = 10
        
        for n in self.niveis:
            if n % 5 == 0:
                divisor-=1

            self.pb += (self.forca + self.percepcao + self.mente) / divisor + (n * 2)

        self.pb = round(self.pb, 2)


    def gerar_aa(self):
        self.aa = (self.forca + self.destreza + self.saude + self.conhecimento + self.mente) / 3
        
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
        

    def gerar_estilo_combate(self, estilo_form):
        niveis = [(1, 1), (2, 10), (11, 20), (21, 30), (31, 40), (41, 50)]

        if estilo_form == "punho_forte":
            vitalidade = [20, 15, 25, 35, 45, 50]
            energia = [20, 15, 25, 35, 45, 50]
            self.destreza += 2
        elif estilo_form == "mente_sagaz":
            vitalidade = [0, 8, 13, 18, 23, 25]
            energia = [40, 22, 37, 52, 67, 75]
            self.mente += 2
        elif estilo_form == "pernas_ageis":
            vitalidade = [25, 18, 31, 43, 56, 62]
            energia = [15, 12, 19, 27, 34, 38]
            self.destreza += 2
        elif estilo_form == "peito_diamante":
            vitalidade = [40, 22, 37, 52, 67, 75]
            energia = [0, 8, 13, 18, 23, 25]
            self.saude += 2
        elif estilo_form == "combate_especializado":
            vitalidade = [15, 12, 20, 27, 34, 38]
            energia = [25, 18, 31, 43, 56, 62]
            self.forca += 1
            self.destreza += 1
        elif estilo_form == "ser_silencio":
            vitalidade = [25, 15, 25, 35, 45, 50]
            energia = [25, 15, 25, 35, 45, 50]
            self.destreza += 1
            self.percepcao += 1
        elif estilo_form == "presenca_imponente":
            vitalidade = [30, 18, 30, 42, 54, 60]
            energia = [20, 12, 20, 28, 36, 40]
            self.comunicacao += 2
        elif estilo_form == "coracao_curativo":
            vitalidade = [10, 8, 13, 18, 23, 25]
            energia = [30, 22, 37, 52, 67, 75]
            self.conhecimento += 1
            self.mente += 1
        else:
            vitalidade = [30, 22, 37, 52, 67, 75]
            energia = [10, 8, 13, 18, 23, 25]
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