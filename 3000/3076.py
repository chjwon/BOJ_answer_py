r,c=map(int,input().split())
a,b=map(int,input().split())
for i in range(r):
    for k in range(a):
        for j in range(c):
            if((i+j)%2==0):
                print('X'*b,end='')
            else:
                print('.'*b,end='')
        print()

# #수리
# a='X'
# b='.'
# R,C = input().split()
# A,B = input().split()
# # print(A,B,R,C)
# for n1 in range(int(C)):
#     for n2 in range(int(A)):
#         for n3 in range(int(R)):
#             for n4 in range(int(B)):
#                 print(a,end='')
#             a , b = b , a
#         a, b = b, a
#         print('\n')
#         a = 'X'
#         b = '.'
#     a, b = b, a














# def printX():
#     for i in range(B):
#         print(a)
#
# def printDot():
#     for i in range(B):
#         print(b)

# def rowXorDot():
#     if (R==R-2*int(R/2)):
#         return 'Dot'
#     else:
#         return 'X'
#
# def columnXorDot():
#     if(C==C-2*int(C/2)):
#         return 'Dot'
#     else:
#         return 'X'
#


