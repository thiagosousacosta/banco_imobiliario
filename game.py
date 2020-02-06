from random import randrange

QUANTIDADE_CASAS        = 20
QUANTIDADE_ROUNDS       = 1000
DINHEIRO_POR_ROUND      = 100
PORCENTAGEM_ALUGUEL     = 0.2

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
            casa.valor_aluguel = casa.valor_casa * PORCENTAGEM_ALUGUEL
            self.casas.append(casa)
            
    def jogar(self):
        for rounds in range(QUANTIDADE_ROUNDS):
            for jogador in self.jogadores:
                
                numero_dado = randrange(1,7)

                if jogador.casa_atual + numero_dado <= QUANTIDADE_CASAS:
                    jogador.casa_atual = jogador.casa_atual + numero_dado
                else: 
                    jogador.casa_atual = (jogador.casa_atual + numero_dado) - QUANTIDADE_CASAS
                    jogador.dinheiro += DINHEIRO_POR_ROUND
                
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
            
            if len(self.jogadores) == 1:
                timeout = 0
                jogador_ganhador = self.jogadores[0].tipo_jogador
                return timeout, jogador_ganhador, rounds

        timeout = 1
        jogador_ganhador = [x.tipo_jogador for x in self.jogadores if x.dinheiro == max([x.dinheiro for x in self.jogadores])][0]
        return timeout, jogador_ganhador, rounds
