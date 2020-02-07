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

    resultado_exigente = (len([x[1] for x in resultado_final if x[1] == 'exigente'] )/QUANTIDADE_SIMULACOES) * 100
    resultado_impulsivo  = (len([x[1] for x in resultado_final if x[1] == 'impulsivo'])/QUANTIDADE_SIMULACOES) * 100
    resultado_cauteloso = (len([x[1] for x in resultado_final if x[1] == 'cauteloso'])/QUANTIDADE_SIMULACOES) * 100
    resultado_aleatorio = (len([x[1] for x in resultado_final if x[1] == 'aleatorio'])/QUANTIDADE_SIMULACOES) * 100
    
    porcentagem_exigente  = round(resultado_exigente)
    porcentagem_impulsivo = round(resultado_impulsivo)
    porcentagem_calteloso = round(resultado_cauteloso)
    porcentagem_aleatorio = round(resultado_aleatorio)

    comportamento_ganhador = statistics.mode([x[1] for x in resultado_final])

    print(f'''
        Partidas Time Out   = {partidas_timeout}
        Média de turnos     = {media_turno}
        
        Resultado Exigente  = {porcentagem_exigente}%
        Resultado Impulsivo = {porcentagem_impulsivo}%
        Resultado Cauteloso = {porcentagem_calteloso}%
        Resultado Aleatório = {porcentagem_aleatorio}%

        Comportamento Ganhador = {comportamento_ganhador}
                ''')