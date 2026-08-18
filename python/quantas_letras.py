a = input()
b = input()
contador = 0

for i in range(len(a)):
    if(b == a[i]):
        contador += 1

print(contador)