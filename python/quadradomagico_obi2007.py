n = int(input())
matriz = []
listaSomaLinha = []
listaSomaColuna = []
listaSomaDiagonal = []
somaLinha = 0
somaColuna = 0
somaDiagonal1 = 0
somaDiagonal2 = 0
contador = ((n-1) * 2) + n + 2

for i in range(n):
    matrizLinha = list(map(int, input().split()))
    matriz.append(matrizLinha)

for i in range(n):
    for j in range(n):
        somaLinha += matriz[i][j]
        somaColuna += matriz[j][i]
        if(i == j):
            somaDiagonal1 += matriz[i][j]
        if(i + j == n - 1):
            somaDiagonal2 += matriz[i][j]

    listaSomaLinha.append(somaLinha)
    somaLinha = 0
    listaSomaColuna.append(somaColuna)
    somaColuna = 0

    if(i == j == n-1):
        listaSomaDiagonal.append(somaDiagonal1)
        listaSomaDiagonal.append(somaDiagonal2)

listaSomaLinha.append(0)
listaSomaColuna.append(0)

for i in range(n):
    if(listaSomaLinha[i] == listaSomaLinha[i+1]):
        contador -= 1
    if(listaSomaColuna[i] == listaSomaColuna[i+1]):
        contador -= 1

for i in range(n):
    if(listaSomaLinha[0] == listaSomaColuna[i]):
        contador -= 1

    if(contador == 2):
        if(listaSomaLinha[0] == listaSomaDiagonal[0] == listaSomaDiagonal[1]):
            contador -= 2

if(contador == 0):
    print(listaSomaLinha[0])
else:
    print("-1")