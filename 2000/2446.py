n = int(input())
num=2*n-1
for i in range(n):
    print(' '*i,end='')
    print('*'*(num-i*2),end='')
    #print(' '*i)
    print()
# 3210 순서되야함 but 밑에는 1234
for i in range(1,n):
    print(' '*(n-i-1),end='')
    print('*'*(2*i+1),end='')
    #print(' '*(n-i-1))
    print()