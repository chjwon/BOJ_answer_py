# 두자리 수 난수생성
# 13이 생성되면 중단

import random

n=int(input('난수의 개수를 입력하세요 : '))
for _ in range(n):
    r=random.randint(10,99)
    print(r,end=' ')
    if r==13 :
        print()
        print('난수 생성을 중단합니다.')
        break
print()
print('난수 생성이 완료되었습니다.')