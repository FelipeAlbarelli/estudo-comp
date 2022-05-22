###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Detector de Palíndromos
# Nome: 
# RA: 
###################################################

# DICA: use os métodos lower, replace, split e index

# Leitura de dados

qnt_linhas_texto = int(input())

# Leitura das linhas do texto e tratamento

pontuacoes = [".", ",", ":", ";", "!", "?"]

palindromos = []
rep_palindromos = []

for _ in range(qnt_linhas_texto):
    linha_cru = input().lower()
    for pontuacao in pontuacoes:
        linha_cru = linha_cru.replace(pontuacao, '')
    linha = linha_cru.split()
    for palavra in linha:
        if palavra in palindromos:
            index_palavra = palindromos.index(palavra)
            rep_palindromos[index_palavra] += 1
            continue
        if palavra == palavra[::-1]:

            palindromos.append(palavra)
            rep_palindromos.append(1)


# Processamento

# Impressão da saída
for palavra, n in zip(palindromos, rep_palindromos):
    print(palavra , n)