def prime_number(num):
    if num != 1:
        for i in range(2,num):
            if(num%i==0):
                return False
    else:
        return False
    return True

min = int(input())
max = int(input())
sol = []
for i in range(min,max+1):
    if prime_number(i):
        sol.append(i)
if(len(sol)==0):
    print(-1)
else:
    print(sum(sol))
    print(sol[0])