n = int(input())
listaNums = list(map(float, input().split()))

for i in range(n):
    raiz = listaNums[i] ** (1/2) 

    print(f"{raiz:.4f}")