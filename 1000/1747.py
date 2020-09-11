def pelindorm(num):
    if(num==int(str(num)[::-1])):
        return True
    else:
        return False

def prime_number(num):
    if num != 1:
        for i in range(2,num):
            if(num%i==0):
                return False
    else:
        return False
    return True

num=int(input())

while(1):
    if(pelindorm(num)==True and prime_number(num)==True):
        print(num)
        break
    else:
        num+=1