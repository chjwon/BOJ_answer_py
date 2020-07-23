a=int(input())
for i in range(a):
    total=0
    n1=input()
    n1=n1.split(' ')
    for i in range(2):
        total+=int(n1[i])
    print(total)