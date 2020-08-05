input_num = []
num = int(input())
for i in range(num):
    temp = int(input())
    input_num.append(temp)

input_num.sort()
for i in range(num):
    print(input_num[i],end = '\n')