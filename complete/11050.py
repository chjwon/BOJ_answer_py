def factorial(x):
    n = 1
    for i in range(1,x+1):
        n = n*i 
    return n

def combination(a,b):
    return (factorial(a)) // ((factorial(a-b))*(factorial(b)))

a,b = map(int,input().split(' '))
print(combination(a,b))