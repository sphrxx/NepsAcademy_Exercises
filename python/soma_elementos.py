n = int(input())
listaNumeros = list(map(int, input().split()))
soma = 0

for i in range(n):
    soma += listaNumeros[i]

print(soma)