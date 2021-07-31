def distanceInOut(x,y,cx,cy):
    return (((x-cx)**2)+((y-cy)**2))**(0.5)

times = int(input())
for _  in range(times):
    x_st, y_st, x_end, y_end = map(int, input().split(' '))
    sol = 0
    circle = int(input())
    for i in range(circle):
        cx, cy, rad = map(int, input().split(' '))
        if ((distanceInOut(x_st,y_st,cx,cy)-rad)*(distanceInOut(x_end,y_end,cx,cy)-rad))<0:
            sol += 1
        else:
            pass
    print(sol)