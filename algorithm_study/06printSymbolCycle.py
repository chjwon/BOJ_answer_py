# *를 n개 출력하지만 m개마다 줄 바꿈
print('*를 출력합니다.')
n=int(input('몇개를 출력할까요? '))
m=int(input('몇개 마다 줄 바꿈 할까요? '))

for i in range(1,n+1):
    print('*',end=' ')
    if(i%m==0):
        print()

# 효율적인 다른 방법
# 위에 것은 for 마다 if 호출되서 비효율

# for _ in range(int(n/m)):
#     print('*'*m)
# print('*'*(n%m))
