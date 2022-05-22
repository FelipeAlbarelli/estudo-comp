###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Eleição 2022
# Nome: 
# RA: 
###################################################

# Leitura no número de candidatos

total_candidatos = int(input())

# Leitura do nome dos candidatos

candidatos = []

for _ in range(total_candidatos):
    nome_candidato = input()
    candidatos.append(nome_candidato)

# Leitura dos votos

votos = []

for i in range(total_candidatos):
    quantidade_votos = int(input())
    votos.append(quantidade_votos)

nulos = int(input())
brancos = int(input())


# calculo do vencedor

total_votos_validos = 0
for voto_atual in votos :
    total_votos_validos += voto_atual

total_votos = total_votos_validos + nulos + brancos

votos_primeiro = 0
votos_segundo  = 0
primeiro  = ''
segundo   = ''

for nome_atual,voto_atual in zip(candidatos , votos):
    # se o candidato da iteração atual tiver mais votos que o primeiro, coloca-lo em primeiro e o antigo primeiro
    # em segundo
    if voto_atual > votos_primeiro:
        votos_segundo = votos_primeiro
        segundo  = primeiro
        votos_primeiro = voto_atual
        primeiro  = nome_atual
    # se for menor que o primeiro, mas maior que o segundo, fazer a troca com o segundo
    elif voto_atual > votos_segundo:
        votos_segundo = voto_atual
        segundo = nome_atual

houve_vencedor = votos_primeiro > (total_votos_validos / 2)


# Impressão das informações de saída


# Se houve vencedor em primeiro turno
if houve_vencedor:
    vencedor = primeiro
    print(vencedor, "foi o vencedor da eleição")

# Se é necessário segundo turno
else :
    print("Haverá segundo turno entre:")
    print(primeiro)
    print(segundo)

print("Total de votos:", total_votos)
print("Votos válidos:", total_votos_validos)