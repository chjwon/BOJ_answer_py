

def prime_number(num):
    if num != 1:
        for i in range(2,num):
            if(num%i==0):
                return False
    else:
        return False
    return True



n = int(input())
sol=0
inputnum = input().split(' ')
for i in range(n):
    inputnum[i]=int(inputnum[i])
    if(prime_number(inputnum[i])==True):
        sol+=1
print(sol)

