student = int(input())
inputList = list(map(int,input().split(' ')))
sol = []
for i in range(student):
    sol.insert(inputList[i],str(i+1))

print(' '.join(reversed(sol)))