input_num = int(input())
list_prime = []

# 소수 판별 함수
def prime_number(num):
    if num != 1:
        for pp in range(2, num):
            if num % pp == 0:
                return False
    else:
        return False
    return True

# 여유롭게 소수의 제곱수 list에 추가
for prime in range(2, input_num-1):
    if prime_number(prime):
        list_prime.append(prime * prime)

# print(list_prime)


# 검수를 위한 제곱수ㄴㄴ list
sol_list = []

# 제곱수 ㄴㄴ 인지 판별  False면 제곱 ㄴㄴ
def solve(number, list_prime):
    flag = True
    for i in range(len(list_prime)):
        if number % list_prime[i] == 0:
            flag = False
    return flag

# 제곱수ㄴㄴ 테스트할 숫자
number = 0

# while의 break을 위한 신호 변수
while_flag = True

while while_flag:
    number += 1
    if solve(number, list_prime):
        sol_list.append(number)
    if len(sol_list) == input_num:
        while_flag = False
        break

sol = sol_list[input_num - 1]

# print(sol_list)
# print('===')

print(sol)
