###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Ballon d'Or
# Nome: 
# RA: 
###################################################

# Leitura de dados

n_votantes = int(input())

jogadores = {}

votos = [6,4,3,2,1]

for _ in range(n_votantes):
    for voto in votos:
        jogador = input()
        if jogador not in jogadores:
            jogadores[jogador] = 0
        jogadores[jogador] += voto

# Processamento



# Impressão da saídas