num = int(input());
sol_list = []
def solution():
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2) + ((y1 - y2) ** 2)
    r=(r1+r2)**2
    rr=(r1-r2)**2
    if(rr==0 and d==0):
        return -1
    elif(r<d or d<rr):
        return 0
    elif(rr<d and d<r):
        return 2
    else:
        return 1
# main
for _ in range(num):
    sol_list.append(solution())
for i in sol_list:
    print(i)