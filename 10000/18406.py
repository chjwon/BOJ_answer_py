num = str(input())
length = len(num) # 6
# print(len(num))

list=[]
list.append(num[0:int(length/2)])
list.append(num[int(length/2):])
# print(list)

temp0=0;temp1=0
for i in range(int(length/2)):
    temp0+=int(list[0][i])
    temp1+=int(list[1][i])

list[0]=temp0
list[1]=temp1
# print(list)

def solution(list):
    if(list[0]==list[1]):
        print("LUCKY")
    else:
        print("READY")

solution(list)

