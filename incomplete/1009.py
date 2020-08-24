# 틀림



num=int(input())
sol=[]
for _ in range(num):
    a,b=map(int,input().split())
    temp =1
    for pp in range(b%10):
        temp = (temp*a)%10
        if(temp==0):
            temp=10
    sol.append(temp)
for i in range(num):
    print(sol[i])