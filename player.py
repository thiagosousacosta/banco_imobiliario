from random import randint

class Jogador():
    def __init__(self, tipo_jogador):
        self.dinheiro = 300
        self.voltas = 0
        self.casa_atual = 0
        self.tipo_jogador = tipo_jogador

    def pode_comprar(self, valor_aluguel, valor_casa):
        if self.tipo_jogador == 'impulsivo':
            if self.dinheiro >= valor_casa:
                return True

        elif self.tipo_jogador == 'exigente':
            if valor_aluguel > 50:
                return True

        elif self.tipo_jogador == 'cauteloso':
            if self.dinheiro - valor_casa >= 80:
                return True

        elif self.tipo_jogador == 'aleatorio':
            if randint(1,10) > 5:
                return True
