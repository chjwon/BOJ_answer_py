list_1=[1,2,3,4,5,6]
list_2=[1,2,3,4,5]

def reverse_list(list_num):
    l = len(list_num)//2
    for i in range(l):
        temp = list_num[len(list_num)-i-1]
        list_num[len(list_num)-i-1] = list_num[i]
        list_num[i] = temp
    return list_num

print(reverse_list(list_1))
print(reverse_list(list_2))