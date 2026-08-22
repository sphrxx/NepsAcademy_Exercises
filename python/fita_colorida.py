qtQuadriculados = int(input())
listaPintados = list(map(int, input().split()))
listaDistancia = []

contadorIncrementa = 0
contadorDecrementa = 0
repetidorAtivo = 1

for i in range(qtQuadriculados):
    if(listaPintados[i] != 0):
        repetidorAtivo = 1

        if(i == 0):
            j = 0
            while(listaPintados[i+j] != 0 and repetidorAtivo == 1):
                if(i+j != qtQuadriculados-1):
                    contadorIncrementa += 1
                    j += 1

                    if(contadorIncrementa >= 9):
                        contadorIncrementa = 9
                        repetidorAtivo = 0

            contadorDecrementa = 999
            

        elif(i < qtQuadriculados-1):
            j = 0
            while(listaPintados[i+j] != 0 and repetidorAtivo == 1):
                if(i+j != qtQuadriculados-1):
                    contadorIncrementa += 1
                    j += 1

                    if(contadorIncrementa >= 9):
                        contadorIncrementa = 9
                        repetidorAtivo = 0

                else:
                    repetidorAtivo = 0
                    contadorIncrementa = 999


            j = 0
            repetidorAtivo = 1

            while(listaPintados[i-j] != 0 and repetidorAtivo == 1):
                if(i-j != 0):
                    contadorDecrementa += 1
                    j += 1

                    if(contadorDecrementa >= 9):
                        contadorDecrementa = 9
                        repetidorAtivo = 0

                else:
                    repetidorAtivo = 0
                    contadorDecrementa = 999

        else:
            j = 0
            while(listaPintados[i-j] != 0 and repetidorAtivo == 1):
                if(i-j != 0):
                    contadorDecrementa += 1
                    j += 1

                    if(contadorDecrementa >= 9):
                        contadorDecrementa = 9
                        repetidorAtivo = 0

                else:
                    repetidorAtivo = 0
                    contadorDecrementa = 999     
                    
            contadorIncrementa = 999
            
        if(contadorIncrementa < contadorDecrementa):
            listaDistancia.append(contadorIncrementa)
        else:
            listaDistancia.append(contadorDecrementa)

        contadorIncrementa = 0
        contadorDecrementa = 0

    else:
        listaDistancia.append(0)

print(*listaDistancia)