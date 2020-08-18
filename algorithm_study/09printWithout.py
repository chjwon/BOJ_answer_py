# a,b 사이를 출력 c를 제외하고
print('출력할 범위를 입력해주세요 : ')
a,b = map(int, input().split(' '))
c = int(input('제외할 수를 입력하세요.'))
for i in range(a,b+1):
    if(i==c):
        continue
    print(i,end=' ')