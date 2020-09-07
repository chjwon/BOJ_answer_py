print("a부터 b까지의 합을 구합니다")
a=int(input('정수 a를 입력하세요 : '))
b=int(input('정수 b를 입력하세요 : '))

def sumAToB(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
    return sum
print(f'{a}부터 {b}까지 정수의 합은 {sumAToB(a,b)}입니다.')
