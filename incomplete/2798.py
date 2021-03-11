N, M = map(int, input().split(' '))
numList = list(map(int,input().split(' ')))

def BlackJack(num1,num2,num3,M,max):
    temp=num1+num2+num3
    if temp < M+1:
        if temp > max:
            return temp
        else:
            return max
    else:
        return max

max = 0

for i1 in range(0,N):
    for i2 in range(1,N-i1):
        for i3 in range(2,N-i2):
            num1 = numList[i1]
            num2 = numList[i2]
            num3 = numList[i3]
            max=BlackJack(num1,num2,num3,M,max)

print(max)
