n = int(input())
numLista = list(map(int, input().split()))
contador = 1
maiorContador = 0

for i in range(n-1):
    if(numLista[i] == numLista[i+1]):
        contador += 1

    else:
        contador = 1

    if(contador > maiorContador):
        maiorContador = contador

print(maiorContador)