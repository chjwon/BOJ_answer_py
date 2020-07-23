num = int(input())
for i in range(1,num+1):
    print('*'*i,end='')
    print(' '*(num*2-i*2),end='')
    print('*'*i,end='')
    print()
for j in range(1,num):
    print('*'*(num-j),end='')
    print(' '*(j*2),end='')
    print('*'*(num-j),end='')
    print()