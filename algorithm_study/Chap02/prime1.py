counter = 0

for n in range(2,1001):
    for i in range(2,n):
        counter+=1
        if n%i ==0: # 나누어 떨어지면 소수가 아님
            break # 반복 생략

    else:
        print(n)
print(f'나눗셈을 실행한 횟수: {counter}')