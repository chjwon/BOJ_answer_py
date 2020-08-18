# 숫자 숫자 숫자
# 형태로 입력하기

def maximum(a,b,c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
        return max


def int_float(a):
    if (a == int(a)):
        return int(a)
    else:
        return a

print("세 숫자의 최댓값을 구합니다.")
print("세 정수를 입력하세요 : ",end=' ')
a,b,c = map(float, input().split(' '))


print(f'최댓값은 : {int_float(maximum(a,b,c))}')