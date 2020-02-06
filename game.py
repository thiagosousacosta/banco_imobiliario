from pdb import set_trace
import random
from player import Jogador

QUANTIDADE_CASAS = 20

class Casa():
    def __init__(self):
        self.numero_casa = 0
        self.valor_casa = 0
        self.valor_aluguel = 0

class Tabuleiro():
    def __init__(self, jogadores):
        
        self.casas = []

        for x in range(QUANTIDADE_CASAS):
            casa = Casa()
            casa.numero_casa = x + 1
            casa.valor_casa = random.randrange(10,200,10)
            casa.valor_aluguel = casa.valor_casa * 0.1
            self.casas.append(casa)

        for jogador in jogadores:
            jogador.dinheiro = 300
        
if __name__ == "__main__":
    jogador1 = Jogador('impulsivo')
    jogador2 = Jogador('exigente')
    jogador3 = Jogador('cauteloso')
    jogador4 = Jogador('aleatorio')

    Tabuleiro([jogador1, jogador2, jogador3, jogador4])