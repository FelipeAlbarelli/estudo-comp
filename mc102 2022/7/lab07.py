###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Encaixe Perfeito
# Nome:
# RA:
###################################################

# Leitura do número de partidas

n = int(input())

for _ in range(n):
  # Leitura das peças 1 e 2
    P1 = [int(i) for i in input().split()]
    P2 = [int(i) for i in input().split()]

    # Processamento das possibilidades de encaixe

    diferenca_tamanho = len(P2) - len(P1)

    melhor_pontuacao = 999999
    encaixe_melhor_pontuacao = 0
    melhor_inverteu  = False

    # iterar sobre todas as maneiras de encaixe

    for inverter in [False , True]:
        for posicao in range(diferenca_tamanho + 1):

            p1_deslocada =   P1[::-1] if inverter else P1
            p2_deslocada =  P2[posicao: len(P1) + posicao ]
            peca_encaixada = [ a + b for a,b in zip(p1_deslocada , p2_deslocada) ]
            
            #encontrar altura máxima
            altura_maxima = 0
            for altura in peca_encaixada:
                if altura > altura_maxima:
                    altura_maxima = altura
            
            soma_diferencas = 0
            #buscar diferenças de encaixe
            for peca in peca_encaixada:
                soma_diferencas += altura_maxima - peca
            
            # checar se é uma jogada melhor
            if soma_diferencas < melhor_pontuacao:
                melhor_pontuacao = soma_diferencas
                melhor_inverteu  = inverter
                encaixe_melhor_pontuacao = posicao + 1 # encaixe começar a contar no 1
        
        
    P = melhor_pontuacao
    R = encaixe_melhor_pontuacao
    S = "Invertida" if melhor_inverteu else "Normal"

    # Impressão da saída esperada para cada partida
    if melhor_pontuacao != 0:
        print("Pontuacao:", P)
    else:
        print("Encaixe Perfeito!")
    print("Posicao de Encaixe:", R)
    print("Peca 1:", S)