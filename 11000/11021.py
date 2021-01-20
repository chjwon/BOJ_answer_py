num = int(input())
sol_list = []
for i in range(num):
    a,b = map(int, input().split(' '))
    sol_list.append(a+b)
for j in range(1,num+1):
    print('Case #'+str(j)+': '+str(sol_list[j-1]))