n = int(input())
listaElementos = list(map(int, input().split()))

listaElementos.sort()

print(*listaElementos)