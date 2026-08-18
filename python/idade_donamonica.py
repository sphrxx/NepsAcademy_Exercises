m = int(input())
f1 = int(input())
f2 = int(input())
f3 = m - (f1 + f2)

if(f1 > f2):
    if(f1 > f3):
        print(f1)
    else:
        print(f3)
elif(f2 > f3):
    print(f2)
else:
    print(f3)