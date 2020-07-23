dice = input().split()

number =[]
for i in range(int(dice[0])*int(dice[1])*int(dice[2])):
    number.append(0)

for d1 in range(1,int(dice[0]) + 1):
    for d2 in range(1,int(dice[1]) + 1):
        for d3 in range(1,int(dice[2]) + 1):
            total = 0
            total=d1 + d2 + d3
            number[total] +=1

print(number.index(max(number)) )