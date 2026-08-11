n1 = int(input())
n2 = int(input())
backupNum = 0
listaValores = []

if(n1 > n2):
    backupNum = n1
    n1 = n2
    n2 = backupNum

for i in range(n1, n2+1):
    listaValores.append(i)

print(*listaValores)