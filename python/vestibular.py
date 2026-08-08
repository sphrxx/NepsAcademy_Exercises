n = int(input())
gabaritoAlternativas = input()
gabaritoCandidato = input()
contador = 0

for i in range(n):
    if(gabaritoAlternativas[i] == gabaritoCandidato[i]):
        contador += 1

print(contador)