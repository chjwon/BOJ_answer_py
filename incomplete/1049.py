def small(a, b):
    if a < b:
        return a
    else:
        return b


total, brand = map(int, input().split(' '))
list_6 = []
list_1 = []
for _ in range(brand):
    temp1, temp2 = map(int, input().split(' '))
    list_6.append(temp1)
    list_1.append(temp2)
list_6.sort()
list_1.sort()

# print(list_1[0],list_6[0])
num6 = total // 6
num1 = total % 6
if num6 > 0:
    solZero = total * list_1[0]
    solOne = (num6 * list_6[0]) + (num1 * list_1[0])
    solTwo = ((num6 - 1) * list_6[0]) + ((num1 + 6) * list_1[0])
    solThree = (num6+1)*list_6[0]
    print(small(small(solZero,solOne),small(solTwo,solThree)))
else:
    print(total * list_1[0])
