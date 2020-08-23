# 모르겠다
# https://www.acmicpc.net/problem/1463



# def calculate(n):
#     if(n%3==0):
#         n=int(n/3)
#     elif(n%2==0):
#         n=int(n/2)
#     else:
#         n-=1
#     return n
#
num=int(input())
# sol=0
# while(1):
#     if(num==1):
#         break
#     else:
#         num=calculate(num)
#         print(num)
#         sol+=1
# print(sol)


print(int(num/3)-1 + (num%3))