print('2자리 양수를 입력하세요')
while 1:
    num = int(input('값을 입력하세요 : '))
    if 10<= num and num <=99:
        break
print(f'입력받은 양수는 {num}입니다.')