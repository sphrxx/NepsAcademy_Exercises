n = int(input())
fibonacci = 1
num1 = 1
num2 = 1

if(n != 0 and n != 1 and n != 2):
    for i in range(n-1):
        num1 = num2
        num2 = fibonacci
        fibonacci = num1 + num2     
else:
    fibonacci = 1

print(fibonacci)