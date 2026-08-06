n1, n2 = map(float, input().split())
media = (n1 + n2) / 2

if(media >= 7):
    print("Aprovado")
elif(media >= 4):
    print("Recuperacao")
else:
    print("Reprovado")