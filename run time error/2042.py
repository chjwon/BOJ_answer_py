# https://www.acmicpc.net/problem/2042
# 런타임에러


def NumChange(b,c,list):
    list[b-1]=c
    return 1

def NumSum(b,c,list):
    ans=0
    for ss in range(b-1,c):
        ans += list[ss]
    print(ans)
    return 1

num_of_numbers, num_of_change, num_of_sum = map(int, input().split(' '))
NumList=[]

for ppp in range(num_of_numbers):
    NumList.append(int(input()))
for i in range(num_of_sum+num_of_change):
    a,b,c = map(int,input().split(' '))
    if(a==1):
        NumChange(b,c,NumList)
    if(a==2):
        NumSum(b,c,NumList)