num = int(input()) ;
if ( num%5 == 0):
    print(int(num/5))
else:
    sol = 0
    while (True):
        num-=3
        if(num<0):
            print(-1)
            break
        sol+=1
        if(num%5==0):
            sol += num/5
            print(int(sol))
            break
