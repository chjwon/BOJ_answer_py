# 시간초과


def min_max(numberList, start, end):
    temp = numberList[start - 1:end]
    return min(temp), max(temp)


# main
a, b = map(int, input().split())
numbers = []
for _ in range(a):
    numbers.append(int(input()))
for __ in range(b):
    srt, end = map(int, input().split(' '))
    print(min_max(numbers, srt, end)[0], ' ', min_max(numbers, srt, end)[1])
