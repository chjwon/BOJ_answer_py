def peoplenum(k, n):
    if n == 1:
        return 1
    elif k == 0:
        return n
    elif k == 1:
        return n * (n + 1) // 2
    else:
        return peoplenum(k - 1, n) + peoplenum(k, n - 1)


case = int(input())
for _ in range(case):
    k = int(input())
    n = int(input())
    print(peoplenum(k, n))
