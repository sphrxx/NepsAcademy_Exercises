operacao = input()
listaNums = list(map(float, input().split()))

if(operacao == 'M'):
    calculo = listaNums[0] * listaNums[1]
    print(f"{calculo:.2f}")
else:
    calculo = listaNums[0] / listaNums[1]
    print(f"{calculo:.2f}")