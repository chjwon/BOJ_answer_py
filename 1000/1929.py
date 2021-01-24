def prime_number(num):
    if num != 1:
        for i in range(2, int(num ** (1 / 2)) + 1):
            if num % i == 0:
                return False
    else:
        return False
    return True


num1, num2 = map(int, input().split(' '))
for i in range(num1, num2+1):
    if prime_number(i):
        print(i)