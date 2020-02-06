from pdb import set_trace
from random import randint, randrange
from player import Jogador

QUANTIDADE_CASAS = 20
QUANTIDADE_ROUNDS = 1000

class Casa():
    def __init__(self):
        self.numero_casa = 0
        self.valor_casa = 0
        self.valor_aluguel = 0
        self.dono_propriedade = ''

class Tabuleiro():
    def __init__(self, jogadores):
        
        self.casas = []
        self.jogadores = jogadores

        for x in range(QUANTIDADE_CASAS):
            casa = Casa()
            casa.numero_casa = x + 1
            casa.valor_casa = randrange(50,500,10)
            casa.valor_aluguel = casa.valor_casa * 0.2
            self.casas.append(casa)
            
    def jogar(self):
        for rounds in range(QUANTIDADE_ROUNDS):
            for jogador in self.jogadores:
                
                numero_dado = randrange(1,7)

                if jogador.casa_atual + numero_dado <= 20:
                    jogador.casa_atual = jogador.casa_atual + numero_dado
                else: 
                    jogador.casa_atual = (jogador.casa_atual + numero_dado) - 20
                    jogador.dinheiro += 100
                
                if self.casas[jogador.casa_atual-1].dono_propriedade == '':
                    if jogador.pode_comprar(self.casas[jogador.casa_atual-1].valor_aluguel, self.casas[jogador.casa_atual-1].valor_casa):
                        self.casas[jogador.casa_atual-1].dono_propriedade = jogador.tipo_jogador
                        jogador.dinheiro - self.casas[jogador.casa_atual-1].valor_casa
                else:
                    dono_propriedade = [x for x in self.jogadores if x.tipo_jogador == self.casas[jogador.casa_atual-1].dono_propriedade][0]
                    jogador.dinheiro -= self.casas[jogador.casa_atual-1].valor_aluguel
                    dono_propriedade.dinheiro += self.casas[jogador.casa_atual-1].valor_aluguel
                
                if jogador.dinheiro < 0:
                    tipo_jogador = jogador.tipo_jogador
                    casas_jogador = [x for x in self.casas if x.dono_propriedade == tipo_jogador]
                    for casa in casas_jogador:
                        casa.dono_propriedade = ''
                    self.jogadores.remove(jogador)
        set_trace()                    

if __name__ == "__main__":
    jogador1 = Jogador('impulsivo')
    jogador2 = Jogador('exigente')
    jogador3 = Jogador('cauteloso')
    jogador4 = Jogador('aleatorio')

    tabuleiro = Tabuleiro([jogador1, jogador2, jogador3, jogador4])
    tabuleiro.jogar()
