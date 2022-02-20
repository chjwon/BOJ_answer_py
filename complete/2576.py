num = []
for _ in range(7):
    temp = int(input())
    if temp % 2 == 1:
        num.append(temp)
if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    num.sort()
    print(num[0])