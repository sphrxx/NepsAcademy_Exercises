vetor = list(map(int, input().split()))
n = int(input())
elementoConfirmacao = 0

for i in range(10):
    if(vetor[i] == n):
        elementoConfirmacao = 1

if(elementoConfirmacao == 1):
    print("SIM")
else:
    print("NAO")