n , c = map(int,input().split(' '))
homePos = []
for _ in range(n):
    homePos.append(int(input()))
    
homePos.sort()

left = 1 # min
right = homePos[-1] # max
sol = 0
flag = True
while flag:
    if left > right:
        flag = False
        break
    mid = (left + right)//2 # set interval (SI)
    current = homePos[0]
    cnt = 1
    for i in range(1,n):
        if homePos[i] - current >= mid: # if interval is more longer than SI
            cnt += 1 # install router
            current = homePos[i] # current position is changed

    if cnt >= c: # if whole quantity of router is greater than c, it is wrong
        sol = mid
        left = mid+1 # increase interval 

    else:
        right = mid - 1 # decrease interval

print(sol)