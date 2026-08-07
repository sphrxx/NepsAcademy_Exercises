n = int(input())
listaDivisores = []

for i in range(1, n+1):
    if(n % i == 0):
        listaDivisores.append(i)

print(*listaDivisores)
        