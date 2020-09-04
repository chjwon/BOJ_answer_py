num=int(input())
for _ in range(num):
    list=input().split()
    for i in range(len(list)):
        print((list[i])[::-1],end=' ')