num=int(input()) ; num=num%8
if(num==0):
    print(2)
elif(num<6):
    print(num)
else:
    print(10-num)