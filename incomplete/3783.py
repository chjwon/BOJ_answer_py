# 어렵당

def solution(number):
    if num < 0:
        number = -number
        number = number ** (1 / 3)
        number = (int(number * (10 ** 10))) / (10 ** 10)
        return -number
    elif num > 0:
        number = number ** (1 / 3)
        number = (int(number * (10 ** 10))) / (10 ** 10)
        return number
    else:
        return 0

# main
num = int(input())
for _ in range(num):
    temp = int(input())
    sol = solution(temp)
    if sol - int(sol) > 0.9999999998:
        sol = int(sol) + 1
    print(format(sol, ".10f"))
