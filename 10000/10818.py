num = int(input())
num_list = input().split()
for i in range(num):
    num_list[i] = int(num_list[i])
def min_max (list):
    list.sort()
    print(list[0], list[-1],sep=' ')
min_max(num_list)