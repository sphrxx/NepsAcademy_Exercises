qtApertado = int(input())
n = list(map(int, input().split()))
int1 = 0
int2 = 0

for i in range (qtApertado):
    if(n[i] % 2 == 1):
        int1 = 1 - int1
    else:
        int1 = 1 - int1
        int2 = 1 - int2

print(int1)
print(int2)