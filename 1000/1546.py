def FixGrade(num,max):
    return num*100/max

a = int(input())
numList = input().split(' ')
for i in range(a):
    numList[i] = int(numList[i])
max = max(numList)
for j in range(a):
    numList[j]=FixGrade(numList[j],max)
print(sum(numList)/a)