def sigma_sum(num):
    return int(num*(num+1)/2)

def Three_sol(N):
    sol = 3*sigma_sum(int(N/3))
    return sol

def Seven_sol(N):
    sol = 7*sigma_sum(int(N/7))
    return sol

def ThreeSeven_sol(N):
    sol = 21 * sigma_sum(int(N / 21))
    return sol

def Sol(N):
    return Three_sol(N) + Seven_sol(N) - ThreeSeven_sol(N)

num = int(input())
list = input().split()
for pp in range(num):
    print(Sol(int(list[pp])))