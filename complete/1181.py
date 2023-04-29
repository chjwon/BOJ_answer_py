import sys
num = int(sys.stdin.readline())
lst = []
for i in range(num):
    lst.append(sys.stdin.readline().strip())
lst_set = set(lst)
lst = list(lst_set)
lst.sort()
lst.sort(key=len)
for i in lst:
    print(i)