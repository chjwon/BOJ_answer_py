#런타임 에러


def isitPrime(n):
    if(n==1):
        return 0
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1



n = int(input())
sol=0
for i in range(n):
    inputnum = list(map(int, input().split()))
for j in range(n):
    sol+= isitPrime(inputnum[j])
print(sol)

