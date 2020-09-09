list=input().split(' ') ; sol = 0
for i in range(5):
    list[i]=int(list[i])
    list[i]=list[i]*list[i]
    sol += list[i]
print(sol%10)