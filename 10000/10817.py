num = input().split(' ')
# print(num)
for i in range(len(num)):
    num[i] = int(num[i])
num.sort()
print(num[1])