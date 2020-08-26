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



list=[]
total=0
for _ in range(9):
    temp=int(input())
    list.append(temp)
    total+=temp

sortlist=quick_sort(list)
# print(total)
# print(sortlist)

sol_num = total-100
solList=[]
sol_yes=False
for i in range(9):
    temp=sol_num-sortlist[i]
    for j in range(i+1,9):
        if(temp==sortlist[j]):
            # solList.append(temp)
            # solList.append(sortlist[i])
            del sortlist[j]
            del sortlist[i]
            # print(sortlist)
            sol_yes=True
            break
    if(sol_yes==True):
        break

for sss in range(len(sortlist)):
    print(sortlist[sss])


