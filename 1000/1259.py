def pelindorm(num):
    if(num==num[::-1]):
        return 'yes'
    else:
        return 'no'

while(1):
    temp=input()
    if(temp=='0'):
        break
    else:
        print(pelindorm(temp))