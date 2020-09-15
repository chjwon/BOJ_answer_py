# 시간초과
# need fix
# https://www.acmicpc.net/problem/2751

#only writting not using
def swap(x, i, j):
    x[i], x[j] = x[j], x[i]

def bubbleSort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i+1]:
                swap(x, i, i+1)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

#================
# a = int(input())
# num = []
# for i in range(a):
#     num.append(int(input()))
# for sol in sorted(num):
#     print(sol)



# main
num = int(input())
list = []
for _ in range(num):
    list.append(int(input()))
list = quick_sort(list)
for j in list:
    print(j)

