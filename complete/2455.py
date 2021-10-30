people = [0]
for _ in range(4):
    a,b = map(int,input().split())
    people.append(people[-1]+b-a)
print(max(people))