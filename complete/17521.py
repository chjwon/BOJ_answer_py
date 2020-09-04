num, money = map(int, input().split(' '))
list=[]
for _ in range(num):
    list.append(int(input()))

# print(list)

for i in range(num-1):
    if(list[i]<list[i+1]):
        x=int(money/list[i])
        money=money%list[i]
        x=x*list[i+1]
        money+=x
print(money)