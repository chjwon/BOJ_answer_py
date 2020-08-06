# need fix
# https://www.acmicpc.net/problem/1712

A,B,C = map(int, input().split(' '))
num = int(A/(C-B))+1
none = -1
if(num>0):
    print(num)
else:
    print(none)