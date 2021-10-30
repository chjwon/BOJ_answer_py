num = int(input())
numList = []
for _ in range(num):
    numList.append(list(map(int,input().split(' '))))
# print(numList)
numList.sort(key=lambda x:(x[1],x[0]))
for i in range(num):
    print(numList[i][0],numList[i][1])