# 시간 초과


def digit_product(num):
    temp=1
    for i in range (len(str(num))):
        temp=temp*int((str(num)[i]))
    return temp

def self_product(num):
    return num*digit_product(num)

a,b=map(int,input().split(' '))
temp=1 ; sol=0
while(1):
    if(a<=self_product(temp) and self_product(temp)<=b):
        # print(temp)
        #
        sol+=1
    else:
        if(temp==int(a)):
            break
    temp+=1

print(sol)