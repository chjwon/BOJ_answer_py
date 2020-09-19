day = int(input())
list=input().split() ; sol=0
for i in range(5):
    if(int(list[i])==day):
        sol+=1
print(sol)