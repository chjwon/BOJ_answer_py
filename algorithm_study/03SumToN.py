# 1에서부터 n까지 정수합
print("1에서부터 n까지 정수합을 구합니다")

while 1:
    num = int(input("n의 값을 입력해주세요 :"))
    if(num>0):
        break

i=1
sum=0

# 1번 덧셈 방법
while i<=num:
    sum +=i
    i+=1

# 2번 덧셈 방법
# for i in range(1,num+1):
#     sum+=i

# 3번 덧셈 방법
# sum = int(num*(num+1)/2)

print(f'1부터 {num}까지 정수의 합은 {sum}입니다.')