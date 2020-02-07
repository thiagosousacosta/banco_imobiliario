from random import randint

class Jogador():
    def __init__(self, tipo_jogador):
        self.dinheiro = 300
        self.voltas = 0
        self.casa_atual = 0
        
        if tipo_jogador == 1:
            self.tipo_jogador = 'Impulsivo'
        elif tipo_jogador == 2:
            self.tipo_jogador = 'Exigente'
        elif tipo_jogador == 3:
            self.tipo_jogador = 'Cauteloso'
        elif tipo_jogador == 4:
            self.tipo_jogador = 'Aleatorio'

    def pode_comprar(self, valor_aluguel, valor_casa):
        if self.tipo_jogador == 'Impulsivo':
            if self.dinheiro >= valor_casa:
                return True

        elif self.tipo_jogador == 'Exigente':
            if valor_aluguel > 50:
                if self.dinheiro >= valor_casa:
                    return True

        elif self.tipo_jogador == 'Cauteloso':
            if self.dinheiro - valor_casa >= 80:
                if self.dinheiro >= valor_casa:
                    return True

        elif self.tipo_jogador == 'Aleatorio':
            if randint(1,10) > 5:
                if self.dinheiro >= valor_casa:
                    return True
