one=0 ; zero = 0;
num=int(input())
for _ in range(num):
    temp=int(input())
    if(temp==0):
        zero+=1
    if(temp==1):
        one+=1
if(zero>one):
    print("Junhee is not cute!")
elif(zero<one):
    print("Junhee is cute!")