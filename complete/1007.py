# python3 제출시 시간 초과
# pypy3 제출시 맞음
# 더 간단한것 생각해야함


import sys
from math import sqrt
read = sys.stdin.readline
minSol=999999999
def solution(idx, cnt):
    global minAns

    if idx == N:
        return
    if cnt == N//2:
        xSum, ySum = 0, 0
        for i in range(N):
            if C[i]:
                xSum += coord[i][0]
                ySum += coord[i][1]
            else:
                xSum -= coord[i][0]
                ySum -= coord[i][1]
        ans = sqrt(xSum * xSum + ySum * ySum)
        if ans < minAns:
            minAns = ans
        return

    solution(idx+1, cnt)
    C[idx] = True
    solution(idx+1, cnt+1)
    C[idx] = False


T = int(read())


while T:
    minAns = 999999999999
    N = int(read())
    C = [False for _ in range(N)]
    coord = []
    for _ in range(N):
        coord.append(list(map(int, read().split())))
    solution(0, 0)
    print("%.12f" % minAns)

    T-=1