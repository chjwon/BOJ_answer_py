flag = True
list=[]
while flag:
    num = float(input())
    if(num==999):
        flag = False
        break
    list.append(num)
# print(list)
for i in range(1,len(list)):
    print(f'%.2f' %(list[i]-list[i-1]))
