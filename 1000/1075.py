num = int(input())
div = int(input())


def lastTwo(num):
    return int(num / 100) * 100


num = lastTwo(num)
num = num % div

if num == 0:
    remain = 0
else:
    remain = div - num


if remain < 10:
    print('0'+str(remain))
else:
    print(str(remain))