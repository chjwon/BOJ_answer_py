nn = input()
list=[]
for i in range(len(nn)):
    list.append(ord(nn[i]))
# print(list)
sol=len(list)
for i in range(len(list)-1):
    if(list[i]<list[i+1]):
        sol-=1
print(sol)