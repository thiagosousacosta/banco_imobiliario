from random import randint

class Jogador():
    def __init__(self, tipo_jogador):
        self.dinheiro = 300
        self.voltas = 0
        self.casa_atual = 0
        
        if tipo_jogador == 1:
            self.tipo_jogador = 'impulsivo'
        elif tipo_jogador == 2:
            self.tipo_jogador = 'exigente'
        elif tipo_jogador == 3:
            self.tipo_jogador = 'cauteloso'
        elif tipo_jogador == 4:
            self.tipo_jogador = 'aleatorio'

    def pode_comprar(self, valor_aluguel, valor_casa):
        if self.tipo_jogador == 'impulsivo':
            if self.dinheiro >= valor_casa:
                return True

        elif self.tipo_jogador == 'exigente':
            if valor_aluguel > 50:
                if self.dinheiro >= valor_casa:
                    return True

        elif self.tipo_jogador == 'cauteloso':
            if self.dinheiro - valor_casa >= 80:
                if self.dinheiro >= valor_casa:
                    return True

        elif self.tipo_jogador == 'aleatorio':
            if randint(1,10) > 5:
                if self.dinheiro >= valor_casa:
                    return True
