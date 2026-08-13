n = int(input())
listaCelulas = []
listaResolvida = []

for i in range(n):
    celula = int(input())
    listaCelulas.append(celula)
    listaResolvida.append(0)

listaCelulas.append(0)

for i in range(n):
    if(listaCelulas[i] == 1):
        listaResolvida[i] += 1

    if(i == 0):
        if(listaCelulas[i+1] == 1):
            listaResolvida[i] += 1
    elif(i >= 1 and i <= n-1):
        if(listaCelulas[i-1] == 1):
            listaResolvida[i] += 1
        if(listaCelulas[i+1] == 1):
            listaResolvida[i] += 1
    else:
        if(listaCelulas[i-1] == 1):
            listaResolvida[i] += 1

    print(listaResolvida[i])