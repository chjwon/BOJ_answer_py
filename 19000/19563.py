a,b,c=map(int, input().split());a=abs(a);b=abs(b)
if((a+b-c)%2==0 and a+b-c<=0):
    print('YES')
else:
    print('NO')