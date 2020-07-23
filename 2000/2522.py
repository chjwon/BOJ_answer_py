n = int(input())
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('*'*i,end='')
    print()
for i1 in range(1,n):
    print(' '*i1,end='')
    print('*'*(n-i1),end='')
    print()