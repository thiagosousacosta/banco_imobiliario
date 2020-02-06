from pdb import set_trace
import random
from player import Jogador

QUANTIDADE_CASAS = 20
QUANTIDADE_JOGADORES = 4

class Casa():
    def __init__(self):
        self.numero_casa = 0
        self.valor_compra = 0
        self.valor_aluguel = 0

class Tabuleiro():
    def __init__(self, jogadores):
        
        self.casas = []

        for x in range(QUANTIDADE_CASAS - 1):
            casa = Casa()
            casa.numero_casa = x + 1
            casa.valor_compra = random.randrange(10,200,10)
            casa.valor_aluguel = casa.valor_compra * 0.1
            self.casas.append(casa)

        for jogador in jogadores:
            jogador.dinheiro = 300
        
        set_trace()

if __name__ == "__main__":
    jogadores = [Jogador() for x in range(QUANTIDADE_JOGADORES)]
    Tabuleiro(jogadores)
    set_trace()