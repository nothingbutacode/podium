from random import random
lista = []

# Criando a matriz dos 6 pilotos e seus 10 tempos.
for i in range (1,7):
    matrizPilotos = []
    piloto = input(f"Digite o nome do {i} piloto: ")
    matrizPilotos.append(piloto)
    for volta in range(0,10):
        x = round(random() * 30 + 90,3)
        matrizPilotos.append(x)
    lista.append(matrizPilotos)

# Descobrindo qual piloto fez a volta mais rápida e em qual volta foi.
melhorVolta = 0
tempoMaisRapido = 121
pilotoMaisRapido = ""
for matrizPilotos in lista:
    voltaAtual = 0

    for volta in matrizPilotos[1:11]:
        temp = volta
        voltaAtual += 1
        
        if temp < tempoMaisRapido:
            pilotoMaisRapido = matrizPilotos[0]
            tempoMaisRapido = temp
            melhorVolta = voltaAtual

# Print da matriz completa com todos os resultados
print("\nTabela de Tempos:\n")
for i in range(0,6):
    print(lista[i])

print(f"\nO piloto {pilotoMaisRapido} teve o tempo mais rapido {tempoMaisRapido} na sua volta número {melhorVolta}\n")

# Criando a matriz da classificação.
tempoMaisRapido = 121
matrizTemp = []
for matrizPilotos in lista:
    voltaAtual = 0
    colunaTemp = []

    for volta in matrizPilotos[1:11]:
        temp = volta
        voltaAtual += 1
        
        if temp < tempoMaisRapido:
            pilotoMaisRapido = matrizPilotos[0]
            tempoMaisRapido = temp
            melhorVolta = voltaAtual
    
    colunaTemp.append(matrizPilotos[0])
    colunaTemp.append(tempoMaisRapido)
    tempoMaisRapido = 121
    colunaTemp.append(melhorVolta)
    matrizTemp.append(colunaTemp)

print("Melhor tempo de cada piloto: \n")
for i in matrizTemp:
    print(i)

#ordenando a matriz de classificação

matrizClassificacao = []
for linha in matrizTemp:
    colunaClassificacao = []
    for j in linha[1:2]:
        colunaClassificacao.append(j)
    matrizClassificacao.append(colunaClassificacao)
    matrizClassificacao.sort()

print("\nPódium:\n")
lugar = 1
for i in matrizClassificacao:
    print(f"{lugar}º Lugar --> {i}")
    lugar += 1


print("\nMédia das voltas:\n")
#Fazendo a matriz transposta 5x10 em 10x5(retirando os nomes), para calcular a media das voltas.
valor = 0
matrizT = []
for i in range(1,11):
    linhaT = []
    for j in range(0,6):
        valor = lista[j][i]
        linhaT.append(valor)
    matrizT.append(linhaT)

#calculando a media das 10 voltas.
media = 0
contador = 0
for i in matrizT:
    soma = 0
    for j in i:
        soma += j
    media = soma/6
    contador += 1
    print("Media da {}ªvolta --> {:.2f}".format(contador,media))