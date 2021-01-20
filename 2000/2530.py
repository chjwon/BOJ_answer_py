H,M,S = map(int, input().split(' '))
t = int(input())
while t>0:
    S+=1
    if(S==60):
        S=0
        M+=1
        if(M==60):
            M=0
            H+=1
            if(H==24):
                H=0
    t-=1
print(H,M,S)