# 런타임


max, variable = map(int, input().split(' '))
numbers=[]
for _ in range(max+1):
    numbers.append('0')

def function(before,variable,num):
    return before * variable + num

for __ in range(max+1):
    temp1,temp2 = map(int, input().split(' '))
    numbers[temp2]=temp1

# print(numbers)


sol=numbers[max]
for i in range(1,max+1):
    sol=function(sol,variable,numbers[max-i])

print(sol)

# sol=function(1,variable,numbers[0])
#
# for i in range(1,max+1):
#     sol=function(sol,variable,numbers[max-i])
#     print(sol)
# print(sol)

# 가장 고전적인 방법 but 시간 초과
# for _ in range(max+1):
#     temp1, temp2 = map(int, input().split(' '))
#     sol += temp1 *(variable**temp2)
# print(sol)
