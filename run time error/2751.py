# 시간초과
# need fix
# https://www.acmicpc.net/problem/2751

#only writting not using
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                swap(x, i, i+1)

#================
a = int(input())
num = []
for i in range(a):
    num.append(int(input()))
for sol in sorted(num):
    print(sol)

