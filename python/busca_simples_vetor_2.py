listaNums = list(map(int, input().split()))
num = int(input())
contador = 0
listaIndices = []

for i in range(10):
    if(listaNums[i] == num):
        contador += 1
        listaIndices.append(i)

if(contador != 0):
    print(contador)
    print(*listaIndices)
else:
    print("Mia x")
    
