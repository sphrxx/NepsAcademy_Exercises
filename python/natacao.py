t1 = int(input())
t2 = int(input())
t3 = int(input())
listaColocados = [0, 0, 0]

if(t1 < t2 and t1 < t3):
    if(t2 < t3):
        listaColocados[0] = 1
        listaColocados[1] = 2
        listaColocados[2] = 3
    else:
        listaColocados[0] = 1
        listaColocados[1] = 3
        listaColocados[2] = 2
elif(t2 < t1 and t2 < t3):
    if(t1 < t3):
        listaColocados[0] = 2
        listaColocados[1] = 1
        listaColocados[2] = 3
    else:
        listaColocados[0] = 2
        listaColocados[1] = 3
        listaColocados[2] = 1
else:
    if(t1 < t2):
        listaColocados[0] = 3
        listaColocados[1] = 1
        listaColocados[2] = 2
    else:
        listaColocados[0] = 3
        listaColocados[1] = 2
        listaColocados[2] = 1

print(listaColocados[0])
print(listaColocados[1])
print(listaColocados[2])