import statistics
from random import sample
from player import Jogador
from game import Tabuleiro

QUANTIDADE_SIMULACOES   = 300

if __name__ == "__main__":
    resultado_final = []
    for x in range(QUANTIDADE_SIMULACOES):
        jogadores = [Jogador(x) for x in sample(range(1,5), 4)]
        tabuleiro = Tabuleiro(jogadores)
        resultado = tabuleiro.jogar()
        resultado_final.append(resultado)

    partidas_timeout = sum([x[0] for x in resultado_final if x[0] == 1])
    media_turno = round(sum([x[2] for x in resultado_final])/QUANTIDADE_SIMULACOES)

    resultado_exigente = (len([x[1] for x in resultado_final if x[1] == 'Exigente'] )/QUANTIDADE_SIMULACOES) * 100
    resultado_impulsivo  = (len([x[1] for x in resultado_final if x[1] == 'Impulsivo'])/QUANTIDADE_SIMULACOES) * 100
    resultado_cauteloso = (len([x[1] for x in resultado_final if x[1] == 'Cauteloso'])/QUANTIDADE_SIMULACOES) * 100
    resultado_aleatorio = (len([x[1] for x in resultado_final if x[1] == 'Aleatorio'])/QUANTIDADE_SIMULACOES) * 100
    
    porcentagem_exigente  = round(resultado_exigente)
    porcentagem_impulsivo = round(resultado_impulsivo)
    porcentagem_calteloso = round(resultado_cauteloso)
    porcentagem_aleatorio = round(resultado_aleatorio)

    comportamento_ganhador = statistics.mode([x[1] for x in resultado_final])

    print(f'''
        Partidas Time Out   = {partidas_timeout}
        Média de turnos     = {media_turno}
        
        Porcentagem de vitória - Exigente  = {porcentagem_exigente}%
        Porcentagem de vitória - Impulsivo = {porcentagem_impulsivo}%
        Porcentagem de vitória - Cauteloso = {porcentagem_calteloso}%
        Porcentagem de vitória - Aleatório = {porcentagem_aleatorio}%

        Comportamento Ganhador = {comportamento_ganhador}
                ''')