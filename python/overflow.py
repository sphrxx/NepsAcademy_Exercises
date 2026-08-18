numMax = int(input())
listaOperacao = list(input().split())
listaOperacao[0] = int(listaOperacao[0])
listaOperacao[2] = int(listaOperacao[2])

if(listaOperacao[1] == '+'):
    calculo = listaOperacao[0] + listaOperacao[2]
    if(calculo > numMax):
        print("OVERFLOW")
    else:
        print("OK")
else:
    calculo = listaOperacao[0] * listaOperacao[2]
    if(calculo > numMax):
        print("OVERFLOW")
    else:
        print("OK")