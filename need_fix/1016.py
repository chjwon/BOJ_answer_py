input_num, input2_num = map(int, input().split())


# 소수 판별 함수
def prime_number(num):
    if num != 1:
        for pp in range(2, num):
            if num % pp == 0:
                return False
    else:
        return False
    return True


# 제곱수 담는 리스트
list_prime = []

for prime in range(2, input2_num - 1):
    if prime_number(prime):
        list_prime.append(prime * prime)

sol_list = []


def solve(number, list):
    flag = True
    for i in range(len(list)):
        if number % list[i] == 0:
            flag = False
            break
    return flag


for pp in range(input_num, input2_num + 1):
    if prime_number(pp):
        sol_list.append(pp)
    else:
        if solve(pp, list_prime):
            sol_list.append(pp)

print(len(sol_list))
