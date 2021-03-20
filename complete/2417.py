num = int(input())
temp = int(num**(1/2))
if temp*temp-num ==0:
    print(temp)
else:
    print(temp+1)