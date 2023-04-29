from collections import deque
import sys
dq = deque([])

num = int(sys.stdin.readline())
for i in range(num):
    dq.append(i+1)
# print(dq)
flag = True
while dq:
    if len(dq) == 1:
        print(dq[0])
        break
    if flag:
        # print(dq)
        dq.popleft()
        flag = False
    else:
        # print(dq)
        dq.append(int(dq.popleft()))
        flag = True
