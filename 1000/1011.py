def sol(num):
    solu = 0
    if num == 1:
        solu = 1
    elif num == 2:
        solu = 2
    else:
        flag = True
        case = 0
        while flag:
            case += 1
            if case*(case + 1) >= num:
                flag = False
                break
            # n(n-1) < num < n(n+1)
        x = case
        y = case * (case + 1) - num
        if y >= x:
            solu = 2*x -1
        else:
            solu = 2*x
    return solu


n = int(input())
for _ in range(n):
    a, b = map(int, input().split(' '))
    print(sol(b-a))
