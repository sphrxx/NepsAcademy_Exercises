x = int(input())
y = int(input())

if(x == 0 or y == 0):
    print("eixos")
elif(x > 0):
    if(y > 0):
        print("Q1")
    else:
        print("Q4")
else:
    if(y > 0):
        print("Q2")
    else:
        print("Q3")
