# main
n = int(input())
numList = input().split()
for i in range(n):
    numList[i] = int(numList[i])

if (n > 2):
    flag = True
    for i in range(0, n - 1, 1):
        if (i == 0):
            current_x = numList[i]  # k
            next_x = numList[i + 1]  # a*k+b
            next2_x = numList[i + 2]  # a^2*k + ab +b
            if(next_x - current_x==0):
                a=0
            else:
                a = int((next2_x - next_x) / (next_x - current_x))
            # (next2_x-next_x) == a^2*k + ab +b - a*k+b == a ((a-1)k+b)
            # (next_x-current_x) == a*k+b - k == (a-1)k+b
            b = next_x - (current_x * a)
            test_array = [numList[0],numList[1]]
        else:
            test_array.append(a*test_array[i]+b)


        if (numList[i+1] != test_array[i+1]):
            flag = False
            break

    if flag:
        print(a*test_array[n-1]+b)
    else:
        print('B')

elif (n == 1):
    # print(numList[0]) # A인가
    print('A')
elif (n == 2):
    if (numList[0] == numList[1]):
        print(numList[0])
    else:
        print('A')
