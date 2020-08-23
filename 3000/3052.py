def uniq(list):
    return [x for i, x in enumerate(list) if x not in list[:i]]

list=[]
for _ in range(10):
    list.append((int(input()))%42)
print(len(uniq(list)))