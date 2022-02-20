for _ in range(3):
    inputList = list(map(int,input().split(' ')))
    zeroCount = inputList.count(0)

    if zeroCount == 0:
        print('E')
    elif zeroCount == 1:
        print('A')
    elif zeroCount == 2:
        print('B')
    elif zeroCount == 3:
        print('C')
    elif zeroCount == 4:
        print('D')
