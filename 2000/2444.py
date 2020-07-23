n = int(input())
for i in range(1,n+1):
    print(' '*(n-i),end='')
    print('*'*(2*i-1))

for i1 in range(1,n):
    print(' ' * i1, end='')
    print('*' * (2 * n - 1 - 2 * i1))