def add_mod10(num1, num2):
    return (num1+num2)%10

def numbers_split (num):
    list_num = [0,0,0,0,0,0,0,0]
    for i in range(8):
        list_num[i] = num%(10**(8-i))

    for j in range(7):
        list_num[j] = int( (list_num[j] - list_num[j+1])/(10**(7-j)))
    return list_num


phone_num1 = int(input())
phone_num2 = int(input())

num1_list = numbers_split(phone_num1)
num2_list = numbers_split(phone_num2)

print(num1_list)
print(num2_list)
