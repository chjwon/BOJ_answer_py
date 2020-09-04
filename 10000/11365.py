list=[]
while(1):
    temp=input()
    if(temp=='END'):
        break
    else:
        list.append(temp)
for i in range(len(list)):
    list[i]=(list[i])[::-1]
    print(list[i])