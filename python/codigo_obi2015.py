n = int(input())
contador = 0
listaBinaria = list(map(int, input().split()))

for i in range(n):
    if(i != n-1 and i != n-2 and listaBinaria[i] == 1 and listaBinaria[i+1] == 0 and listaBinaria[i+2] == 0):
        contador += 1

print(contador)