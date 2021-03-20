def one(list, num):
    list.append(num)


def two(list, num):
    list.remove(num)


def three(list):
    print(sum(list))


def four(list):
    temp = list[0]
    for i in range(1,len(list)):
        temp = temp ^ list[i]
    print(temp)


num = int(input())
main_list = [0]
for _ in range(num):
    temp = input()
    if ' ' in temp:
        temp1 = int(temp[0])
        temp2 = int(temp[2])
        if temp1 == 1:
            one(main_list, temp2)
        elif temp1 == 2:
            two(main_list, temp2)
    else:
        temp = int(temp)
        if temp == 3:
            three(main_list)
        elif temp == 4:
            four(main_list)
