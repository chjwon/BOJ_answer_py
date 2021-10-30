from itertools import combinations
card,number = map(int,input().split(' '))
cardList = list(map(int,input().split(' ')))
comb = combinations(cardList,3)
sol = []
# print(list(comb))
for i in list(comb):
    if sum(i) <= number:
        sol.append(sum(i))
sol.sort()
print(sol[-1])