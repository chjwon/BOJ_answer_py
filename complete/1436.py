end = '666'
n = int(input())
cnt = 0
sol = 666
flag = True
while flag:
    if end in str(sol):
        cnt += 1
    if cnt == n:
        print(sol)
        flag = False
        break
    else:
        sol += 1