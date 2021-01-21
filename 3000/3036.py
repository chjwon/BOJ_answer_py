def gcd(x,y):
    while y:
        x, y = y, x % y
    return x

n = int (input())
numList = list(map(int, input().split(' ')))
first = numList[0]
for i in range(1,n):
    print(str(int(first/(gcd(first,numList[i]))))+'/'+str(int(numList[i]/gcd(first,numList[i]))))