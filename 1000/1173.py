#while을 이용하여 1회당 실패 조건만 필터
#x는 현재 맥박 sol는 답안
N, m, M, T, R = map(int,input().split())
x,sol=m,0
while N>0:
    sol +=1
    if(x+T<=M):
        x+=T
        N-=1
        continue
    if(x-R>=m):
        x-=R
    else:
        x=m
    if(x==m and x+T>M):
        sol=-1
        break
print(sol)





# 정규식으로 -1에 대한 조건을 찾으려했지만 실패
# N, m, M, T, R = map(int,input().split())
# rest = 0
# no = -1
# a = (m+N*T-M)/R
# if(a==int(a)):
#     rest = int(a)
# else:
#     rest = int(a)+1
# if(m+T>M):
#     print(no)
# elif((T-R)*N+m>M):
#     print(no)
# elif(a<0):
#     print(no)
# else:
#     print(rest+N)