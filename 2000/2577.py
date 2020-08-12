a=int(input())
b=int(input())
c=int(input())
num=a*b*c
num=str(num)
number=['0','1','2','3','4','5','6','7','8','9']
for i in range(10):
    number[i] = num.count(number[i])
    print(number[i])