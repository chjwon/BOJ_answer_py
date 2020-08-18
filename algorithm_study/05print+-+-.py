# +와 - 반복 교차 출력
print('+와 -를 번갈아 출력합니다.')
num = int(input('몇개를 출력할까요?: '))
for i in range(num):
    if(i%2==0):
        print('+',end=' ')
    else:
        print('-',end=' ')

# 또 다른 방법
# for _ in range(int(num/2):
#     print('+ -',end=' ')
# if num%2==1:
#     print('+')

print()