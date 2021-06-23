a,p = map(int, input().split(' '))
numbers = [a]
past_num = [0]*250000
past_num[a]=[1]

flag = True
while flag:
    t = numbers[-1]
    temp = 0
    while t:
        temp += ((t%10)**p)
        t//=10
    if not past_num[temp] :
        numbers.append(temp)
        past_num[temp]=1
    else:
        numbers = numbers[:numbers.index(temp)]
        flag = False
        break

print(str(len(numbers)))
