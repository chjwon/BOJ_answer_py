num = int(input())
if(num <10):
    num = '0'+str(num)
else:
    num=str(num)
temp = str(num[1]) + str(((int(num[0]) + int(num[1]))) % 10)
sol=1
while(1):
    if(num==temp):
        break
    temp = str(temp[1]) + str(((int(temp[0]) + int(temp[1]))) % 10)
    #print(temp)
    sol+=1
print(sol)