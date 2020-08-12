list=[]
for i in range(5):
    list.append(int(input()))
sol = 0
for ss in range(5):
    if(list[ss] > 40):
        sol += list[ss]
    else:
        sol += 40
print(int(sol/5))