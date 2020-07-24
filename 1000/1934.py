def Maxnum(a,b):
    sol1 = 0
    if(a>b):
        a,b=b,a
    for i in range(1,a+1):
        if(a%i==0 and b%i==0):
            sol1 = i
    return sol1

n=int(input())
for i in range(n):
    num1, num2 = map(int, input().split())
    print(int(num1*num2/Maxnum(num1,num2)))