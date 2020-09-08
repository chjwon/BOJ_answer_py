num = int(input())

FiboList=[(1,0),(0,1)]
for i in range(2,41):
    f = FiboList[i-2][0] + FiboList[i-1][0]
    s = FiboList[i-2][1] + FiboList[i-1][1]
    FiboList.append((f,s))

for j in range(num):
    n = int(input())
    result = FiboList[n]
    print("{0} {1}".format(result[0],result[1]))