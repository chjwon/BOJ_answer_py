# 시간 초과
# need fix
# https://www.acmicpc.net/problem/2869
a,b,c = map(int, input().split(' ')) ; sol = 0
def dal (a,b,c,sol):
    while(1):
        sol += 1
        if(c<0 or c==0):
            return sol
        c-=a
        if (c < 0 or c == 0):
            return sol
        c += b
print(dal(a,b,c,sol))