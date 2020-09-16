def del_string(num, string):
    num-=1
    string = string[0:num]+string[num+1:]
    return string
num=int(input())
for _ in range(num):
    num, st = input().split(' ')
    print(del_string(int(num),st))
