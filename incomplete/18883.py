# 틀렸음
# 왜 그럴까

a,b = map(int, input().split())
for i in range(a):
    for j in range(1,b+1):
        print(i*4+j,end=' ')
    print(end='\n')