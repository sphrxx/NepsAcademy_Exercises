n1 = int(input())
n2 = int(input())
mediaPonderada = ((n1*2)+(n2*3))/5

if(mediaPonderada >= 7):
    print("Aprovado")
elif(mediaPonderada < 3):
    print("Reprovado")
else:
    print("Final")