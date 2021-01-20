num = int(input())

for i in range(num):
    for j in range(num*2):
        if(i+j)%2 == 0:
            print('*',end='')
        else:
            print(' ',end='')
    print()



