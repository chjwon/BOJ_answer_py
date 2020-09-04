import sys
n = int(sys.stdin.readline())
for _ in range(n):
    test = sys.stdin.readline()
    tmp = 0
    res = 0
    for a in test:
        if a == 'O':
            tmp += 1
            res += tmp
        else:
            tmp = 0
    print(res)