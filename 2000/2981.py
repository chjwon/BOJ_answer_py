import math

num = int(input())
list = []  # input 정수들
list2 = []  # 최대공약수의 약수들
gcd = 0  # 01,12를 각각 뺀 최대공약수
for i in range(num):
    list.append(int(input()))
    if i == 1:
        gcd = abs(list[1] - list[0])
    gcd = math.gcd(abs(list[i] - list[i - 1]), gcd)
gcd_a = int(gcd ** 0.5)

for i in range(2, gcd_a + 1):
    if gcd % i == 0:
        if i not in list2:
            list2.append(i)
        if gcd // i not in list2:
            list2.append(gcd // i)

list2.append(gcd)
list2.sort()
# list2 = sorted(list2)

for i in list2:
    print(i, end=' ')
