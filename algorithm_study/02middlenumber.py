# 세 숫자의 중앙값 구하기
# function

def med3(a,b,c):
    if(a>=b):
        if(b>=c):
            return b
        elif (a<=c):
            return a
        else:
            return c
    elif (a>c):
        return a
    elif (b>c):
        return c
    else:
        return b

# 같은 방식으로
# def med3(a,b,c):
#     if(c<=a and a<=b) or (b<=a and a<=c):
#         return a
#     elif(c<=b and b<=a) or (a<=b and b<=c):
#         return b
#     else:
#         return c


def int_float(a):
    if (a == int(a)):
        return int(a)
    else:
        return a


print("세 숫자중 중앙값을 구합니다.")
print("세 정수를 입력하세요 : ",end=' ')
a,b,c = map(float, input().split(' '))

print(f'중앙값은 {int_float(med3(a,b,c))}입니다.')