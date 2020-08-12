# need fix
# https://www.acmicpc.net/problem/1920
# 런타임에러

num1=0
num2=0
num1_arr=[]
num2_arr=[]
sol=[]
zero = 0

num1=int(input())
for n1 in range(num1):
    a = input()
    num1_arr.append(a)

num2 = int(input())
for n2 in range(num2):
    b=input()
    num2_arr.append(b)
    sol.append(zero)

n1=0;n2=0

for n2 in range(num2):
    for n1 in range(num1):
        if(num2_arr[n2]==num1_arr[n1]):
            sol[n2]=1
for i in range(len(sol)):
    print(sol[i])