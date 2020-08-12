list=[]
for i in range(5):
    list.append(int(input()))
print(str(min(list[0],list[1],list[2])+(min(list[3],list[4]))-50))