numBandejas = int(input())
coposQuebrados = 0

for i in range (numBandejas):
    latas, copos = map(int, input().split()) 

    if(latas > copos):
        coposQuebrados += copos

print(coposQuebrados)