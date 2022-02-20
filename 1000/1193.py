num = int(input())
n = 1
flag = True
while flag:
    if n * (n + 1) // 2 >= num:
        flag = False
        break
    n += 1
temp = n * (n + 1) // 2 - num
if n % 2:
    print(str(temp + 1) + '/' + str(n - temp))
else:
    print(str(n - temp) + '/' + str(temp + 1))
